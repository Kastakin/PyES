import logging

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
        # Charge values of comps
        self.comp_charge = data["compModel"]["Charge"]
        # Data relative to the species and solid species
        self.species_data = data["speciesModel"]
        self.solid_data = data["solidSpeciesModel"]
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
        if self.initl >= self.finall:
            raise Exception("Initial -log[A] should be lower then final -log[A].")

        if self.linc == 0:
            raise Exception("Increment of -log[A] should be more then zero.")

        # Create two arrays (log and conc. of indipendent component)
        self.ind_comp_logs = np.arange(self.initl, (self.finall + self.linc), self.linc)
        self.ind_comp_c = 10 ** (-self.ind_comp_logs)

        # Calculate the number of points in the interval
        self.nop = len(self.ind_comp_c)

        # Check if the number of points in the range of pH is greater then 0
        if self.nop == 0:
            raise Exception("Number of points in the -log[A] range shouldn't be 0.")

        # Analytical concentration of each component (including the ones that will be ignored)
        self.c_tot = self.conc_data.iloc[:, 0].copy().to_numpy(dtype="float")

        # Check if thay are all zero
        if (self.c_tot == 0).all():
            raise Exception(
                "Analytical concentration shouldn't be zero for all components."
            )

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

        # Store the stechiometric coefficients for the components
        # IMPORTANT: each component is considered as a species with logB = 0
        comp_model = np.identity(self.nc, dtype="int")

        # Ignore the rows relative to the flagged as ignored species and solid species
        species_not_ignored = self.species_data.loc[
            self.species_data["Ignored"] == False
        ]
        solid_not_ignored = self.solid_data.loc[self.solid_data["Ignored"] == False]

        # Store the stechiometric coefficients for the species and solid species
        base_model = species_not_ignored.iloc[:, 8:-1].to_numpy(dtype="int").T
        solid_model = solid_not_ignored.iloc[:, 8:-1].to_numpy(dtype="int").T

        # Stores log_betas and log_ks of not ignored species
        base_log_beta = species_not_ignored.iloc[:, 2].to_numpy(dtype="float")
        solid_log_ks = solid_not_ignored.iloc[:, 2].to_numpy(dtype="float")

        # Store comp_names
        self.comp_names = self.conc_data.index
        ignored_comp_names = self.comp_names[ignored_comps]
        self.comp_names = np.delete(self.comp_names, ignored_comps, 0)

        # Store for each species which component is used to calculate relative percentage.
        self.species_perc_str = species_not_ignored.iloc[:, -1].to_numpy(dtype="str")
        self.solid_perc_str = solid_not_ignored.iloc[:, -1].to_numpy(dtype="str")

        # Remove all the species and solid species that have one or more ignored comp with not null coeff.
        # with their relative betas and component for percentage computation
        species_to_remove = (base_model[ignored_comps, :] != 0).sum(axis=0) != 0
        solid_to_remove = (solid_model[ignored_comps, :] != 0).sum(axis=0) != 0
        base_model = np.delete(base_model, species_to_remove, axis=1)
        solid_model = np.delete(solid_model, solid_to_remove, axis=1)
        base_log_beta = np.delete(base_log_beta, species_to_remove, axis=0)
        solid_log_ks = np.delete(solid_log_ks, solid_to_remove, axis=0)
        self.species_perc_str = np.delete(
            self.species_perc_str, species_to_remove, axis=0
        )
        self.solid_perc_str = np.delete(self.solid_perc_str, solid_to_remove, axis=0)

        # Delete the columns for the coeff relative to the ignored components
        base_model = np.delete(base_model, ignored_comps, axis=0)
        solid_model = np.delete(solid_model, ignored_comps, axis=0)

        # Transforms the component used to calculate percentages from string to the corresponding index
        # If any of the species or solid species would use one of the ignored comps
        # assign the index for computation as if the indipendent comp
        # would be used instead (its percent value will be zero)
        self._percEncoder(ignored_comp_names)

        # Assemble the models and betas matrix
        self.model = np.concatenate((comp_model, base_model), axis=1)
        self.log_beta_ris = np.concatenate(
            (np.array([0 for i in range(self.nc)]), base_log_beta), axis=0
        )
        self.solid_model = solid_model
        self.solid_log_ks = solid_log_ks

        # Get the number of not-ignored species/solid species
        self.ns = base_model.shape[1]
        self.nf = solid_model.shape[1]

        # Number of components and number of species/solids has to be > 0
        if self.nc <= 0 | (self.ns <= 0 & self.nf <= 0):
            raise Exception(
                "Number of components and number of not ignored species should be more then zero."
            )

        # Check the ionic strength mode
        # Load the required data if so
        self.imode = data["imode"]
        if self.imode == 1:
            # Load reference ionic strength
            self.species_ris = species_not_ignored.iloc[:, 4].to_numpy(dtype="float")
            self.solid_ris = solid_not_ignored.iloc[:, 4].to_numpy(dtype="float")
            # Remove ionic strenght for species/solids that are ignored
            self.species_ris = np.delete(self.species_ris, species_to_remove, axis=0)
            self.solid_ris = np.delete(self.solid_ris, solid_to_remove, axis=0)
            # If ref. ionic strength is not given for a point use the reference one
            self.species_ris = np.where(
                self.species_ris == 0, data["ris"], self.species_ris
            )
            self.solid_ris = np.where(self.solid_ris == 0, data["ris"], self.solid_ris)
            # Add ref. ionic strength for components
            self.species_ris = np.insert(
                self.species_ris, 0, [data["ris"] for i in range(self.nc)]
            )
            # Calculate square root of reference ionic strength for species
            self.radqris = np.sqrt(self.species_ris)

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
            self.cg = species_not_ignored.iloc[:, 5].to_numpy(dtype="float")
            self.dg = species_not_ignored.iloc[:, 6].to_numpy(dtype="float")
            self.eg = species_not_ignored.iloc[:, 7].to_numpy(dtype="float")
            self.cg = np.delete(self.cg, species_to_remove, axis=0)
            self.dg = np.delete(self.dg, species_to_remove, axis=0)
            self.eg = np.delete(self.eg, species_to_remove, axis=0)
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
        self.species_names = self._speciesNames(self.model, self.comp_names)
        logging.info("--- DATA LOADED ---")

    def predict(self):
        """
        Given the loaded data returns species distribution.
        """
        # Calculate species distribution
        # Return formatted species distribution as a nice table
        logging.info("--- BEGINNING CALCULATION --- ")
        species, solid, log_b, ionic_strength = self._compute()

        # Set the flag to signal a completed run
        self.done_flag = True

        # Create the table containing the species/comp. concentration
        self.species_distribution = pd.DataFrame(
            species,
            index=self.ind_comp_logs,
            columns=self.species_names,
        ).rename_axis(
            index="p[" + self.comp_names[self.ind_comp] + "]",
            columns="Species Con. [mol/L]",
        )

        # Create the table containing the solid species "concentration"
        self.solid_distribution = pd.DataFrame(
            solid, index=self.ind_comp_logs
        ).rename_axis(
            index="p[" + self.comp_names[self.ind_comp] + "]",
            columns="Solid Con. [mol/L]",
        )

        # Compute and create table with percentages of species with respect to component
        # As defined with the input
        cans = np.insert(self.c_tot[0], self.ind_comp, 0)
        can_to_perc = np.concatenate(
            (cans, [cans[index] for index in self.species_perc_int]), axis=0
        )

        adjust_factor = np.array(
            [
                self.model[component, self.nc + index]
                for index, component in enumerate(self.species_perc_int)
            ]
        )
        adjust_factor = np.where(adjust_factor <= 0, 1, adjust_factor)
        adjust_factor = np.concatenate(
            ([1 for component in range(self.nc)], adjust_factor), axis=0
        )

        perc_table = np.where(
            can_to_perc == 0, 0, (species * adjust_factor) / can_to_perc
        )
        perc_table = perc_table * 100

        # Percentages are rounded two the second decimal and stored in a dataframe
        self.species_percentages = (
            pd.DataFrame(
                perc_table,
                index=self.ind_comp_logs,
                columns=[self.species_names, self.species_perc_str],
            )
            .rename_axis(
                index="p[" + self.comp_names[self.ind_comp] + "]",
                columns=["Species", r"% relative to comp."],
            )
            .round(2)
        )

        # If working at variable ionic strength
        if self.imode == 1:
            # Add multi index to the species distribution containing the ionic strength
            self.species_distribution.insert(0, "I", ionic_strength)
            self.species_distribution.set_index("I", append=True, inplace=True)

            # Create table containging adjusted LogB for each point
            self.log_beta = pd.DataFrame(
                log_b[:, self.nc :],
                index=self.ind_comp_logs,
                columns=self.species_names[self.nc :],
            ).rename_axis(
                index="p[" + self.comp_names[self.ind_comp] + "]",
                columns="Formation Constants",
            )
            self.log_beta.insert(0, "I", ionic_strength)
            self.log_beta.set_index("I", append=True, inplace=True)

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

    def solidDistribution(self):
        """
        Returns the solid species concentration table.
        """
        if self.done_flag == True:
            return self.solid_distribution
        else:
            return False

    def formationConstants(self):
        """
        Returns the table containing formation costants and the ionic strength.
        """
        if self.done_flag == True:
            return self.log_beta
        else:
            return False

    def percentages(self):
        """
        Return percentages of species with respect to the desired component.
        """
        if self.done_flag == True:
            return self.species_percentages
        else:
            return False

    def parameters(self):
        """
        Returns relevant data that was used for the computation
        """
        if self.done_flag == True:
            species_info = pd.DataFrame(
                {
                    "logB": self.log_beta_ris[self.nc :],
                },
                index=self.species_names[self.nc :],
            ).rename_axis(index="Species Names")

            if self.imode == 1:
                species_info.insert(1, "Ref. I", self.species_ris[self.nc :])
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
        else:
            return False

    def _compute(self):
        """
        Calculate species distribution.
        """
        # Initialize array to contain the species concentration
        # obtained from the calculations
        results_species_conc = []
        results_solid_conc = []
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

                if (c < 0).any():
                    c = lp1

                # Convert logs back to concentrations
                c = 10 ** (-c)
                c[self.ind_comp] = fixed_c

                cp = results_solid_conc[(point - 1)]
                logging.debug("ESTIMATED C WITH INTERPOLATION")
            elif point > 0:
                c = results_species_conc[(point - 1)][: self.nc].copy()
                c[self.ind_comp] = fixed_c

                cp = results_solid_conc[(point - 1)]
                logging.debug("ESTIMATED C FROM PREVIOUS POINT")
            elif point == 0:
                c = np.multiply(self.c_tot[0], 0.01)
                c = np.insert(c, self.ind_comp, fixed_c)
                cp = np.array([0 for solid in range(self.nf)])
                logging.debug("ESTIMATED C AS FRACTION TOTAL C")

            logging.debug("INITIAL ESTIMATED FREE C: {}".format(c))
            logging.debug("TOTAL C: {}".format(self.c_tot[point]))

            # Calculate species concnetration or each curve point
            (
                species_conc_calc,
                solid_conc_calc,
                log_b,
                ionic_strength,
            ) = self._newtonRaphson(
                point,
                c,
                cp,
                self.model,
                self.solid_model,
                self.log_beta_ris,
                self.solid_log_ks,
                self.c_tot[point],
                fixed_c,
                self.nc,
                self.ns,
                self.nf,
            )

            # Store calculated species concentration into a vector
            results_species_conc.append(species_conc_calc)
            # Store calculated solid species
            results_solid_conc.append(solid_conc_calc)
            # Store calculated ionic strength
            results_ionic_strength.append(ionic_strength)
            # Store calculated LogB
            results_log_b.append(log_b)

        # Stack calculated species concentration/logB/ionic strength in tabular fashion
        results_species_conc = np.stack(results_species_conc)
        results_solid_conc = np.stack(results_solid_conc)
        results_ionic_strength = np.stack(results_ionic_strength)
        results_log_b = np.stack(results_log_b)

        # Return distribution/logb/ionic strength
        return (
            results_species_conc,
            results_solid_conc,
            results_log_b,
            results_ionic_strength,
        )

    def _newtonRaphson(
        self,
        point,
        c,
        cp,
        model,
        solid_model,
        log_beta_ris,
        solid_log_ks,
        c_tot,
        fixed_c,
        nc,
        ns,
        nf,
    ):
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
            else:
                log_beta = self.previous_log_beta

            logging.debug("Estimate of LogB for point {}: {}".format(point, log_beta))

            c, c_spec = self._damping(
                point, c, cp, log_beta, c_tot, model, solid_model, nc, ns, nf
            )
            log_beta, cis = self._updateLogB(c_spec, log_beta_ris, self.species_charges)
            self.previous_log_beta = log_beta
            logging.debug("Updated LogB: {}".format(log_beta))
        else:
            log_beta = log_beta_ris
            c, c_spec = self._damping(
                point, c, cp, log_beta, c_tot, model, solid_model, nc, ns, nf
            )
            cis = [None]

        # Calculate total concentration given the species concentration
        c_tot_calc, c_spec = self._speciesConcentration(
            c, cp, model, solid_model, log_beta, nc, ns, nf
        )
        # Compute difference between total concentrations
        can_delta = c_tot - c_tot_calc
        saturation_index = self._saturationIndex(c, nf, solid_model, solid_log_ks)
        solid_delta = [1 for solid in range(nf)] - saturation_index
        delta = np.concatenate((can_delta, solid_delta))

        for iteration in range(200):
            logging.debug(
                "-> BEGINNING NEWTON-RAPHSON ITERATION {} ON POINT {}".format(
                    iteration, point
                )
            )

            # Compute Jacobian
            J = self._computeJacobian(
                nc, nf, model, solid_model, c_spec, saturation_index
            )
            # Calculate shift to free concentration
            # indipendent component shift is kept at 0 (not altered)
            shifts = np.linalg.solve(J, delta)
            shifts = np.insert(shifts, self.ind_comp, 0, axis=0)
            logging.debug(
                "Shifts to be applied to concentrations and precipitates: {}".format(
                    shifts
                )
            )
            # Positive constrain on freeC as present in STACO
            for index, shift in enumerate(shifts[:nc]):
                if shift <= -c[index]:
                    logging.debug(
                        "Positivizing Shift relative to component number {}".format(
                            index
                        )
                    )
                    factor = -0.99 * c[index] / shift
                    shifts = factor * shifts

            for index, shift in enumerate(shifts[nc:]):
                if shift <= -cp[index]:
                    logging.debug(
                        "Positivizing Shift relative to precipitate number {}".format(
                            index
                        )
                    )
                    factor = -0.99 * cp[index] / shift
                    shifts = factor * shifts

            # Apply shift to free concentrations
            c = c + shifts[:nc]
            cp = cp + shifts[nc:]
            logging.debug(
                "Shifts actually applied to concentrations and precipitates: {}".format(
                    shifts
                )
            )
            logging.debug("Newton-Raphson updated free concentrations: {}".format(c))
            logging.debug(
                "Newton-Raphson updated precipitate concentrations: {}".format(cp)
            )

            # TODO: check if damping is really useful after each N-R iteration
            # # Damp after newton-raphson iteration
            # c, c_spec = self._damping(point, c, cp, log_beta, c_tot, model, solid_model, nc, ns, nf)

            # Calculate total concentration given the updated free/precipitate concentration
            c_tot_calc, c_spec = self._speciesConcentration(
                c, cp, model, solid_model, log_beta, nc, ns, nf
            )

            # Compute difference between total concentrations and convergence
            can_delta = c_tot - c_tot_calc
            saturation_index = self._saturationIndex(c, nf, solid_model, solid_log_ks)
            solid_delta = [1 for solid in range(nf)] - saturation_index
            delta = np.concatenate((can_delta, solid_delta))

            comp_conv_criteria = np.sum(can_delta / c_tot) ** 2

            logging.debug(
                "Convergence for analytical concentrations at Point {} iteration {}: {}".format(
                    point, iteration, comp_conv_criteria
                )
            )

            # If convergence criteria is met return the result
            if (comp_conv_criteria < 1e-16) and (all(i < 1e-16 for i in solid_delta)):
                return c_spec, cp, log_beta, cis[0]

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

    def _computeJacobian(self, nc, nf, model, solid_model, c_spec, saturation_index):
        nt = nc + nf
        # print("{}NC {}NF {}NT".format(nc, nf, nt))
        # print(model)
        # print(solid_model)
        # print(saturation_index)
        # Initiate the matrix for jacobian
        J = np.zeros(shape=(nt, nt))

        # Compute Jacobian
        # Jacobian for acqueous species
        for j in range(nc):
            for k in range(nc):
                J[j, k] = np.sum(model[j] * model[k] * (c_spec / c_spec[k]))
        # print("done species")
        # Jacobian for solid species
        for j in range(nc):
            for k in range(nc, nt):
                # print("computing {},{}".format(j, k))
                J[j, k] = solid_model[j, (k - nc)]
        # print("done first protion solids")

        for j in range(nc, nt):
            for k in range(nc):
                # print("computing {},{}".format(j, k))
                J[j, k] = solid_model[k, (j - nc)] * (
                    saturation_index[(j - nc)] / c_spec[k]
                )
        # print("done second protion solids")

        for j in range(nc, nt):
            for k in range(nc, nt):
                # print("computing {},{}".format(j, k))
                J[j, k] = 0

        # Ignore row and column relative to the indipendent component
        J = np.delete(J, self.ind_comp, axis=0)
        J = np.delete(J, self.ind_comp, axis=1)
        # print("done with jacobian")
        return J

    # TODO: document added functions
    def _speciesConcentration(self, c, cp, model, solid_model, log_beta, nc, ns, nf):
        """
        Calculate species concentration it returns c_spec and c_tot_calc:
        - c_spec[0->nc] = free conc for each component.
        - c_spec[nc+1->nc+ns] = species concentrations.
        - c_tot_calc = estimated anaytical concentration.
        """
        log_c = np.log10(c)
        tiled_log_c = np.tile(log_c, [ns + nc, 1]).T
        log_spec_mat = tiled_log_c * model
        log_c_spec = np.sum(log_spec_mat, axis=0) + log_beta
        log_c_spec = self._checkOverUnderFlow(log_c_spec)
        c_spec = 10 ** log_c_spec
        logging.debug("Species Concentrations: {}".format(c_spec))

        tiled_cp = np.tile(cp, [nc, 1])

        # Estimate total concentration given the species concentration
        c_tot_calc = np.sum(model * np.tile(c_spec, [nc, 1]), axis=1) + (
            np.sum(solid_model * tiled_cp, axis=1) if nf > 0 else 0
        )
        # Take out the analytical concentration relative to the indipendent component
        c_tot_calc = np.delete(c_tot_calc, self.ind_comp, 0)
        logging.debug("Calculated Total Concentration: {}".format(c_tot_calc))

        return c_tot_calc, c_spec

    def _checkOverUnderFlow(self, log_c_spec):
        log_c_spec = np.where(log_c_spec > self.epsl, self.epsl, log_c_spec)
        log_c_spec = np.where(log_c_spec < -self.epsl, -self.epsl, log_c_spec)
        return log_c_spec

    def _damping(self, point, c, cp, log_beta, c_tot, model, solid_model, nc, ns, nf):
        logging.debug("ENTERING DAMP ROUTINE")

        c_tot_calc, c_spec = self._speciesConcentration(
            c, cp, model, solid_model, log_beta, nc, ns, nf
        )

        ## ES42020 METHOD

        clim1 = np.abs(c_tot) / 4
        clim2 = np.abs(c_tot) * 4

        damp_iteration = 0
        jrc = 1
        # TODO: this subroutine could be vectorized to make it faster
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
                c, cp, model, solid_model, log_beta, nc, ns, nf
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

    def _saturationIndex(self, c, nf, solid_model, solid_log_ks):
        if nf > 0:
            tiled_c = np.tile(c, [nf, 1]).T
            saturation_index = np.prod(
                (tiled_c ** solid_model) / (10 ** solid_log_ks), axis=0
            )
            return saturation_index
        else:
            return np.array([])

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
            + self.cg * (cis - self.species_ris)
            + self.dg * ((cis * radqcis) - (self.species_ris * self.radqris))
            + self.eg * ((cis ** 2) - (self.species_ris ** 2))
        )

        return updated_log_beta, cis

    def _percEncoder(self, ignored_comp_names):
        comp_encoder = dict(zip(self.comp_names, range(self.comp_names.shape[0])))
        invalid_comp_encoder = dict(
            zip(ignored_comp_names, range(len(ignored_comp_names)))
        )
        species_perc_int = self.species_perc_str
        solid_perc_int = self.solid_perc_str
        self.species_perc_str = np.concatenate(
            (self.comp_names, self.species_perc_str), axis=0
        )
        for key, value in comp_encoder.items():
            species_perc_int = np.where(
                species_perc_int == key, value, species_perc_int
            )
            solid_perc_int = np.where(solid_perc_int == key, value, solid_perc_int)
        for key, value in invalid_comp_encoder.items():
            species_perc_int = np.where(
                species_perc_int == key, self.ind_comp, species_perc_int
            )
            solid_perc_int = np.where(
                solid_perc_int == key, self.ind_comp, solid_perc_int
            )

        self.species_perc_int = species_perc_int.astype(int)
        self.solid_perc_int = solid_perc_int.astype(int)

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
