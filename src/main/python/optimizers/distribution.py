import logging
import math

import numpy as np
import pandas as pd


class Distribution:
    """
    Newton-Raphson method to solve iterativly mass balance equations.
    """

    def __init__(self):
        # Set limit for underflow/overflow exp
        self.epsl = 200
        # Set flag to report that computation is done
        self.done_flag = False

    def fit(self, data):
        """
        Loads the data used to optimize the system.

        :param data: data as given from the GUI.
        """
        logging.info("--- START DATA LOADING ---")

        # Comp names
        self.comps = data["compModel"]["Name"]
        # Charge values of comps
        self.comp_charge = data["compModel"]["Charge"]
        # Data relative to the species and solid species
        self.species_data = data["speciesModel"]
        self.solid_species_data = data["solidSpeciesModel"]
        # Data relative to comp concentrations
        self.conc_data = data["concModel"]

        # Indipendent comp
        self.ind_comp = data["ind_comp"]
        # Initial log value
        self.initl = data["initialLog"]
        # Final log value
        self.finall = data["finalLog"]
        # log increments at each point
        self.linc = data["logInc"]

        # Final log value should be higher then the initial one
        if self.initl > self.finall:
            raise Exception("Initial -log[A] should be lower then final -log[A].")

        # Create two arrays (log and conc. of indipendent component)
        # np.arange can return values higher then the desired amount, so we trim those out
        self.nop = round((self.finall - self.initl) / self.linc)
        self.ind_comp_logs = np.linspace(self.initl, self.finall, self.nop)
        self.ind_comp_c = 10 ** (-self.ind_comp_logs)

        # Calculate the number of points in the interval
        # self.nop = len(self.ind_comp_c)

        # Check if the number of points in the range of pH is greater then 0
        if self.nop == 0:
            raise Exception("Number of points in the -log[A] range shouldn't be 0.")

        # Analytical concentration of each component (including the ones that will be ignored)
        self.c_tot = self.conc_data.iloc[:, 0].copy().to_numpy(dtype="float")

        # Charges of components
        self.comp_charge = self.comp_charge.copy().to_numpy(dtype="int")

        self.c_tot = np.delete(self.c_tot, self.ind_comp, 0)
        # Find which components have to be ignored (c0 = 0)
        ignored_comps = np.where(self.c_tot == 0)[0]

        # Remove the concentration and charge data relative to those
        self.c_tot = np.delete(self.c_tot, ignored_comps, 0)
        self.comp_charge = np.delete(self.comp_charge, ignored_comps)

        # get number of effective components
        self.nc = int(len(self.conc_data)) - len(ignored_comps)

        # for every ignored comp which index is lower
        # of the designated indipendent comp
        # reduce its index by one (they "slide over")
        self.ind_comp = self.ind_comp - (ignored_comps < self.ind_comp).sum()

        # Assign the indipendent component concentration for each point
        self.c_tot = np.tile(self.c_tot, [self.nop, 1])

        # Define the stechiometric coefficients for the various species
        # IMPORTANT: each component is considered as a species with logB = 0
        aux_model = np.identity(self.nc, dtype="int")

        # Ignore the rows relative to the flagged as ignored species
        species_not_ignored = self.species_data.loc[
            self.species_data["Ignored"] == False
        ]
        base_model = species_not_ignored.iloc[:, 7:].to_numpy(dtype="int").T

        # Stores log_betas of not ignored species
        base_log_beta = species_not_ignored.iloc[:, 1].to_numpy(dtype="float")

        # Remove all the species that have one or more ignored comp with not null coeff.
        # with their relative betas
        to_remove = (base_model[ignored_comps, :] != 0).sum(axis=0) != 0
        base_model = np.delete(base_model, to_remove, axis=1)
        base_log_beta = np.delete(base_log_beta, to_remove, axis=0)

        # Delete the columns for the coeff relative to those components
        base_model = np.delete(base_model, ignored_comps, axis=0)

        # Assemble the model and betas matrix
        self.model = np.concatenate((aux_model, base_model), axis=1)
        self.log_beta_ris = np.concatenate(
            (np.array([0 for i in range(self.nc)]), base_log_beta), axis=0
        )

        # Get the number of not-ignored species
        self.ns = base_model.shape[1]

        # TODO: this will break the code sooner or later when phases will be introduced
        self.nf = int(
            len(self.solid_species_data) - self.solid_species_data.Ignored.sum()
        )

        # Number of components and number of species has to be > 0
        if self.nc <= 0 | (self.ns <= 0 & self.nf <= 0):
            raise Exception(
                "Number of components and number of species have to be > 0."
            )

        # Check the ionic strength mode
        # Load the required data if so
        self.imode = data["imode"]
        if self.imode == 1:
            # Load reference ionic strength
            self.ris = species_not_ignored.iloc[:, 3].to_numpy(dtype="float")
            self.ris = np.delete(self.ris, to_remove, axis=0)
            # If ref. ionic strength is not given for a point use the reference one
            self.ris = np.where(self.ris == 0, data["ris"], self.ris)
            # Add ref. ionic strength for components
            self.ris = np.insert(self.ris, 0, [data["ris"] for i in range(self.nc)])
            self.radqris = np.sqrt(self.ris)

            # Load background ions concentration
            self.bs = data["cback"]

            a = data["a"]
            self.b = data["b"]
            c0 = data["c0"]
            c1 = data["c1"]
            d0 = data["d0"]
            d1 = data["d1"]
            e0 = data["e0"]
            e1 = data["e1"]

            # Check if default have to be used
            if (a == 0) & (self.b == 0):
                a = 0.5
                self.b = 1.5

            # Compute p* for alla the species
            past = self.model.sum(axis=0) - 1

            # Reshape charges into a column vector
            comp_charge_column = np.reshape(self.comp_charge, (self.nc, 1))
            # Same vector except missing the charge of the indipendent component, used later in the computation
            self.comp_charge_no_indipendent = np.delete(self.comp_charge, self.ind_comp)

            # Compute species charges
            self.species_charges = (self.model * comp_charge_column).sum(axis=0)

            # Compute z* for all the species
            zast = (self.model * (comp_charge_column ** 2)).sum(axis=0) - (
                self.species_charges
            ) ** 2

            # Compute A/B term of D-H equation
            self.az = a * zast
            self.fib = self.radqris / (1 + (self.b * self.radqris))

            # Retrive CG/DG/EG for each of the species
            # Remove values that refers to ignored comps
            self.cg = species_not_ignored.iloc[:, 4].to_numpy(dtype="float")
            self.dg = species_not_ignored.iloc[:, 5].to_numpy(dtype="float")
            self.eg = species_not_ignored.iloc[:, 6].to_numpy(dtype="float")
            self.cg = np.delete(self.cg, to_remove, axis=0)
            self.dg = np.delete(self.dg, to_remove, axis=0)
            self.eg = np.delete(self.eg, to_remove, axis=0)
            # Adds values for components
            self.cg = np.insert(self.cg, 0, [0 for i in range(self.nc)])
            self.dg = np.insert(self.dg, 0, [0 for i in range(self.nc)])
            self.eg = np.insert(self.eg, 0, [0 for i in range(self.nc)])

            to_compute = (self.cg == 0) + (self.dg == 0) + (self.eg == 0)

            # Compute CG/DG/EG terms of D-H
            default_cg = c0 * past + c1 * zast
            default_dg = d0 * past + d1 * zast
            default_eg = e0 * past + e1 * zast

            self.cg = np.where(to_compute, default_cg, self.cg)
            self.dg = np.where(to_compute, default_dg, self.dg)
            self.eg = np.where(to_compute, default_eg, self.eg)

        # Compose species names from the model
        self.comp_names = self.conc_data.index
        self.comp_names = np.delete(self.comp_names, ignored_comps, 0)
        self.species_names = self._speciesNames(self.model, self.comp_names)
        logging.info("--- DATA LOADED ---")

    def predict(self):
        """
        Given the loaded data returns species distribution.
        """
        # Calculate species distribution
        # Return formatted species distribution as a nice table
        logging.info("--- BEGINNING CALCULATION --- ")
        species, log_b, ionic_strength = self._compute()

        # Set the flag to signal a completed run
        self.done_flag = True

        self.species_distribution = pd.DataFrame(
            species,
            index=self.ind_comp_logs,
            columns=self.species_names,
        ).rename_axis(
            index="p[" + self.comp_names[self.ind_comp] + "]",
            columns="Species Con. [mol/L]",
        )

        # If working at variable ionic strength
        if self.imode == 1:
            # Add column to the species distribution containing the ionic strength
            self.species_distribution.insert(0, "I", ionic_strength)

            # Create table for the adjusted LogB at each point
            self.log_beta = pd.DataFrame(
                log_b[:, self.nc :],
                index=self.ind_comp_logs,
                columns=self.species_names[self.nc :],
            ).rename_axis(
                index="p[" + self.comp_names[self.ind_comp] + "]",
                columns="Formation Constants",
            )
            self.log_beta.insert(0, "I", ionic_strength)

        logging.info("--- CALCULATION TERMINATED ---")

        return True

    def distribution(self):
        """
        Returns the species concentration table.
        """
        if self.done_flag == True:
            return self.species_distribution
        else:
            return False

    def formation_constants(self):
        """
        Returns the table containing formation costants and the ionic strength.
        """
        if self.done_flag == True:
            return self.log_beta
        else:
            return False

    def parameters(self):
        """
        Returns relevant data that was used for the computation
        """
        species_info = pd.DataFrame(
            {
                "logB": self.log_beta_ris[self.nc :],
            },
            index=self.species_names[self.nc :],
        ).rename_axis(index="Species Names")

        if self.imode == 1:
            species_info.insert(1, "Ref. I", self.ris[self.nc :])
            species_info.insert(2, "Charge", self.species_charges[self.nc :])
            species_info.insert(3, "C", self.cg[self.nc :])
            species_info.insert(4, "D", self.dg[self.nc :])
            species_info.insert(5, "E", self.eg[self.nc :])

        comp_info = pd.DataFrame(
            {
                "Charge": self.comp_charge,
                "Tot. C.": np.insert(self.c_tot[0], self.ind_comp, None),
            },
            index=self.species_names[: self.nc],
        ).rename_axis(index="Components Names")

        return species_info, comp_info

    def _compute(self):
        """
        Calculate species distribution.
        """
        # Initialize array to contain the species concentration
        # obtained from the calculations
        results_species_conc = []
        results_log_b = []
        results_ionic_strength = []

        # Cycle over each point of titration
        for point in range(self.nop):
            logging.debug("--> OPTIMIZATION POINT: {}".format(point))

            # Calculate species concentration given initial betas
            # Initial guess of free concentration (c) is considered as follows:
            #   - First point as a fraction of the total concentration
            #   - Second and third points as estimate from previous point
            #   - Subsequent points are extrapolated as follows

            fixed_c = self.ind_comp_c[point]

            if point > 2:
                lp1 = -np.log10(results_species_conc[(point - 1)][: self.nc])
                lp2 = -np.log10(results_species_conc[(point - 2)][: self.nc])
                lp3 = -np.log10(results_species_conc[(point - 3)][: self.nc])

                # If two subsequent points present the same concentration
                # avoid the issue by using simply the previous point concentration
                c = np.where(lp2 == lp3, lp1, (lp1 + ((lp1 - lp2) ** 2) / (lp2 - lp3)))
                # If the extrapolation returns valuse that would cause under/overflow adjust them accordingly
                c = np.where(c > (self.epsl / 2), (self.epsl / 2), c)
                c = np.where(c < (-self.epsl / 2), (-self.epsl / 2), c)
                # Converto logs back to concentrations
                c = 10 ** (-c)
                c[self.ind_comp] = fixed_c
                logging.debug("ESTIMATED C WITH INTERPOLATION")
            elif point > 0:
                c = results_species_conc[(point - 1)][: self.nc].copy()
                c[self.ind_comp] = fixed_c
                logging.debug("ESTIMATED C FROM PREVIOUS POINT")
            elif point == 0:
                c = np.multiply(self.c_tot[0], 0.01)
                c = np.insert(c, self.ind_comp, fixed_c)
                logging.debug("ESTIMATED C AS FRACTION TOTAL C")

            logging.debug("INITIAL ESTIMATED FREE C: {}".format(c))
            logging.debug("TOTAL C: {}".format(self.c_tot[point]))

            # Calculate species concnetration or each curve point
            species_conc_calc, log_b, ionic_strength = self._newtonRaphson(
                point,
                c,
                self.model,
                self.log_beta_ris,
                self.c_tot[point],
                fixed_c,
                self.nc,
                self.ns,
                self.nf,
            )

            # Store calculated species concentration into a vector
            results_species_conc.append(species_conc_calc)
            # Store calculated ionic strength
            results_ionic_strength.append(ionic_strength)
            # Store calculated LogB
            results_log_b.append(log_b)

        # Stack calculated species concentration/logB/ionic strength in tabular fashion
        results_species_conc = np.stack(results_species_conc)
        results_ionic_strength = np.stack(results_ionic_strength)
        results_log_b = np.stack(results_log_b)

        # Return distribution/logb/ionic strength
        return results_species_conc, results_log_b, results_ionic_strength

    def _newtonRaphson(self, point, c, model, log_beta_ris, c_tot, fixed_c, nc, ns, nf):
        # FIXME: FOR DEBUGGING PURPOSES
        np.seterr("print")

        # If working with variable ionic strength ompute initial guess for species concentration
        if self.imode == 1:
            if point == 0:
                log_beta, _ = self._updateLogB(
                    c_tot,
                    log_beta_ris,
                    self.comp_charge_no_indipendent,
                    first_guess=True,
                )
                logging.debug("Estimate LogB for point 0: {}".format(log_beta))
            else:
                log_beta = self.previous_log_beta

            c, c_spec = self._damping(point, c, log_beta, c_tot, model, nc, ns, nf)
            log_beta, cis = self._updateLogB(c_spec, log_beta_ris, self.species_charges)
            self.previous_log_beta = log_beta
            logging.debug("Updated LogB: {}".format(log_beta))
        else:
            log_beta = log_beta_ris
            cis = [None]

        # Calculate total concentration given the species concentration
        c_tot_calc, c_spec = self._speciesConcentration(c, model, log_beta, nc, ns, nf)
        # Compute difference between total concentrations
        delta = c_tot - c_tot_calc

        for iteration in range(200):
            logging.debug(
                "-> BEGINNING ITERATION {} ON POINT {}".format(iteration, point)
            )

            # Initiate the matrix for jacobian
            J = np.zeros(shape=(nc, nc))

            # Compute Jacobian
            for j in range(nc):
                for k in range(j, nc):
                    J[j, k] = np.sum(model[j] * model[k] * c_spec)
                    J[k, j] = J[j, k]

            # Ignore row and column relative to the indipendent component
            J = np.delete(J, self.ind_comp, axis=0)
            J = np.delete(J, self.ind_comp, axis=1)

            # Calculate shift to free concentration
            # The free concentration vector is manipulated so
            # that the same value for the indipendent component is kept
            c = np.delete(c, self.ind_comp, axis=0)
            delta_c = np.linalg.solve(J, delta) * c
            delta_c = np.insert(delta_c, self.ind_comp, 0, axis=0)
            c = np.insert(c, self.ind_comp, fixed_c, axis=0)

            # Positive constrain on freeC as present in STACO
            for i, shift in enumerate(delta_c):
                if shift <= -c[i]:
                    logging.debug(
                        "Positivizing Shift relative to component number {}".format(i)
                    )
                    factor = -0.99 * c[i] / shift
                    delta_c = factor * delta_c

            # Apply shift to free concentrations
            c = c + delta_c
            logging.debug("Newton-Raphson updated free concentrations: {}".format(c))

            # Damp after newton-raphson iteration
            c, c_spec = self._damping(point, c, log_beta, c_tot, model, nc, ns, nf)

            # Calculate total concentration given the damped free concentration
            c_tot_calc, c_spec = self._speciesConcentration(
                c, model, log_beta, nc, ns, nf
            )

            # Compute difference between total concentrations and convergence
            delta = c_tot - c_tot_calc
            conv_criteria = np.sum(delta / c_tot) ** 2

            logging.debug(
                "Convergence at Point {} iteration {}: {}".format(
                    point, iteration, conv_criteria
                )
            )

            # If convergence criteria is met return the result
            if conv_criteria < 1e-10:
                return c_spec, log_beta, cis[0]

        else:
            logging.error(
                "Calculation terminated early, no convergence found at point {}".format(
                    point
                )
            )
            raise Exception(
                "Calculation of species concentration aborted, no convergence found with conc {} at point {}".format(
                    str(c_spec), point
                )
            )

    # TODO: document added functions
    def _speciesConcentration(self, c, model, log_beta, nc, ns, nf):
        # Calculate species concentration (c_spec[0->nc]=free conc/c_spec[nc+1->nc+ns]=species conc)
        log_c = np.log10(c)
        tiled_log_c = np.tile(log_c, [ns + nc, 1]).T
        log_spec_mat = tiled_log_c * model
        log_c_spec = np.sum(log_spec_mat, axis=0) + log_beta
        log_c_spec = np.where(log_c_spec > self.epsl, self.epsl, log_c_spec)
        log_c_spec = np.where(log_c_spec < -self.epsl, -self.epsl, log_c_spec)
        c_spec = 10 ** log_c_spec
        logging.debug("Species Concentrations: {}".format(c_spec))

        # Estimate total concentration given the species concentration
        c_tot_calc = np.sum(model * np.tile(c_spec, [nc, 1]), axis=1)
        # Take out the analytical concentration relative to the indipendent component
        c_tot_calc = np.delete(c_tot_calc, self.ind_comp, 0)
        logging.debug("Calculated Total Concentration: {}".format(c_tot_calc))

        return c_tot_calc, c_spec

    def _damping(self, point, c, log_beta, c_tot, model, nc, ns, nf):
        logging.debug("ENTERING DAMP ROUTINE")
        # TODO: Dampening of free concentration

        c_tot_calc, c_spec = self._speciesConcentration(c, model, log_beta, nc, ns, nf)

        ## ES42020 METHOD

        clim1 = np.abs(c_tot) / 4
        clim2 = np.abs(c_tot) * 4

        damp_iteration = 0
        jrc = 1
        while damp_iteration < 200:
            fmin = 1
            fmax = 1
            for i, calc_c in enumerate(c_tot_calc):
                if abs(calc_c) < (clim1[i] / jrc) or abs(calc_c) > (clim2[i] / jrc):
                    fatt = abs(c_tot[i] / calc_c)
                    if fatt < fmin:
                        m1 = i
                        fmin = fatt
                    elif fatt > fmax:
                        m2 = i
                        fmax = fatt
                    else:
                        pass

            if fmin != 1:
                fatt = fmin
                j = m1
            elif fmax != 1:
                fatt = fmax
                j = m2
            else:
                logging.debug("EXITING DAMP ROUTINE")
                return c, c_spec

            exp = np.max(model[j]) ** (-1 / 1)
            logging.debug(
                "Damping {} by a factor {} to the power of {}".format(j, fatt, exp)
            )
            c[j] = c[j] * fatt ** exp
            logging.debug("Damped C: {}".format(c))

            c_tot_calc, c_spec = self._speciesConcentration(
                c, model, log_beta, nc, ns, nf
            )

            if np.isnan(c_tot_calc).any():
                raise Exception(
                    "Damping routine got invalid values: {} at point {}".format(
                        c, point
                    )
                )

            damp_iteration += 1
            if (damp_iteration == 200) & (jrc == 1):
                damp_iteration = 0
                jrc = 2

    def _ionicStr(self, c, charges, first_guess):
        """
        Calculate ionic strength given concentrations of species and their charges.
        """
        if first_guess:
            I = ((c * (charges ** 2)).sum() / 2) + self.bs
        else:
            I = ((c * (charges ** 2)).sum() + self.bs) / 2

        return I

    def _updateLogB(self, c, log_beta, charges, first_guess=False):
        """
        Update formation costants from the reference ionic strength to the current one.
        """
        cis = self._ionicStr(c, charges, first_guess)
        logging.debug("Current I: {}".format(cis))
        cis = np.tile(cis, self.nc + self.ns)
        radqcis = np.sqrt(cis)
        fib2 = radqcis / (1 + (self.b * radqcis))
        updated_log_beta = (
            log_beta
            - self.az * (fib2 - self.fib)
            + self.cg * (cis - self.ris)
            + self.dg * ((cis * radqcis) - (self.ris * self.radqris))
        )

        return updated_log_beta, cis

    def _speciesNames(self, model, comps):
        """
        Returns species names as brute formula from comp names and coefficients
        """
        model = model.T
        names = []

        # TODO: vectorize the operation
        for i in range(len(model)):
            names.append("")
            for j, comp in enumerate(comps):
                if model[i][j] < 0:
                    names[i] = names[i] + ("(OH)")
                else:
                    names[i] = names[i] + ("(" + comp + ")") * (
                        1 if model[i][j] != 0 else 0
                    )
                if model[i][j] >= 2 or model[i][j] < -1:
                    names[i] = names[i] + str(abs(model[i][j]))
                else:
                    pass

        return names
