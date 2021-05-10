import logging
import math

import numpy as np
import pandas as pd


class Titration:
    """
    Newton-Raphson method to solve iterativly mass balance equations.
    """

    def __init__(self):
        self.epsl = 200

    def fit(self, data):
        """
        Loads the data used to optimize the system.

        :param data: data as given from the GUI.
        """
        logging.info("--- START DATA LOADING ---")
        # Get number of components
        self.nc = data["nc"]

        # Comp names
        self.comp_name = data["compModel"]["Name"]
        # Charge values of comps
        self.comp_charge = data["compModel"]["Charge"]
        # Data relative to the species and solid species
        self.species_data = data["speciesModel"]
        self.solid_species_data = data["solidSpeciesModel"]
        # Data relative to comp concentrations
        self.conc_data = data["concModel"]

        # Analytical concentration of each component
        self.c_tot = self.conc_data.iloc[:, 0].copy().to_numpy(dtype="float")

        # Concentration in the titrant for each component
        self.c_added = self.conc_data.iloc[:, 1].copy().to_numpy(dtype="float")

        # Initial volume
        self.v0 = data["v0"]
        # First titration point volume
        self.initv = data["initv"]
        # Volume increment at each point
        self.vinc = data["vinc"]
        # number of points
        self.nop = int(data["nop"])

        # Initial volume should be higher then v0
        if self.v0 > self.initv:
            raise Exception(
                "Initial titration volume should be higer or equal to initial volume."
            )
        # Check if the number of points in the range of pH is greater then 0
        if self.nop == 0:
            raise Exception("Number of points in the titration is 0.")

        self.v_added = np.array([[self.vinc * x for x in range(self.nop)]])
        v1_diff = self.initv - self.v0
        self.v_added += v1_diff
        self.v_tot = self.v0 + self.v_added

        # Total concentration corrected for v_tot
        # logging.debug("one {}".format(np.tile(self.c_tot, [self.nop, 1]) * self.v0))
        # logging.debug("two: {}".format(np.tile(self.v_added, [self.nc, 1]).T * self.c_added))
        self.c_tot_adj = (
            np.tile(self.c_tot, [self.nop, 1]) * self.v0
            + np.tile(self.v_added, [self.nc, 1]).T * self.c_added
        ) / np.tile(self.v_tot, [self.nc, 1]).T

        # Get the number of not-ignored species
        self.ns = int(len(self.species_data) - self.species_data.Ignored.sum())
        self.nf = int(len(self.solid_species_data) - self.solid_species_data.Ignored.sum())

        # Number of components and number of species has to be > 0
        if self.nc <= 0 | (self.ns <= 0 & self.nf <= 0):
            raise Exception(
                "Number of components and number of species have to be > 0."
            )

        # Define the stechiometric coefficients for the various species
        # IMPORTANT: each component is considered as a species with logB = 0
        aux_model = np.identity(self.nc, dtype="int")
        species_not_ignored = self.species_data.loc[
            self.species_data["Ignored"] == False
        ]
        base_model = species_not_ignored.iloc[:, 7:].to_numpy(dtype="int").T
        self.model = np.concatenate((aux_model, base_model), axis=1)
        # Stores log_betas
        base_log_beta = species_not_ignored.iloc[:, 1].to_numpy(dtype="float")
        self.log_beta = np.concatenate(
            (np.array([0 for i in range(self.nc)]), base_log_beta), axis=0
        )

        # Compose species names from the model
        self.species_names = self._speciesNames(self.model, self.conc_data.index)
        logging.info("--- DATA LOADED ---")

    def predict(self):
        """
        Given the loaded data returns species distribution.
        """
        # Calculate species distribution
        # Return formatted species distribution as a nice table
        logging.info("--- BEGINNING CALCULATION --- ")
        final_result = self._residuals()
        self.species_distribution = pd.DataFrame(
            final_result,
            index=self.v_added[0],
            columns=self.species_names,
        ).rename_axis(index="V. Added [ml]", columns="Species Con. [mol/L]")
        logging.info("--- CALCULATION TERMINATED ---")

        return True

    def distribution(self):
        return self.species_distribution

    # FIXME: not used for the time being
    # def potential(self):
    #     return self.pot_calc

    def _residuals(self):
        """
        Calculate species distribution.
        """
        # Initialize array to contain the species concentration
        # obtained from the calculations
        results_species_conc = []

        # Cycle over each point of titration
        for point in range(self.nop):
            logging.debug("--> OPTIMIZATION POINT: {}".format(point))

            # Calculate species concentration given initial betas
            # Initial guess of free concentration (c) is considered as follows:
            #   - First point as a fraction of the total concentration
            #   - Second and third points as estimate from previous point
            #   - Subsequent points are extrapolated as follows

            if point > 3:
                v = self.v_added[0, point]
                v1 = self.v_added[0, (point - 1)]
                v2 = self.v_added[0, (point - 2)]
                v3 = self.v_added[0, (point - 3)]
                lp1 = -np.log10(results_species_conc[(point - 1)][: self.nc])
                lp2 = -np.log10(results_species_conc[(point - 2)][: self.nc])
                lp3 = -np.log10(results_species_conc[(point - 3)][: self.nc])
                c = lp1 + (((lp1 - lp2) / (v1 - v2)) ** 2) * (
                    (v2 - v3) / (lp2 - lp3)
                ) * (v - v1)
                c = 10 ** (-c)
                logging.debug("ESTIMATED C WITH INTERPOLATION")
            elif point > 0:
                c = results_species_conc[(point - 1)][: self.nc]
                logging.debug("ESTIMATED C FROM PREVIOUS POINT")
            elif point == 0:
                c = np.multiply(self.c_tot_adj[0], 0.001)
                logging.debug("ESTIMATED C AS FRACTION TOTAL C")

            logging.debug("INITIAL ESTIMATED FREE C: {}".format(c))
            logging.debug("TOTAL C: {}".format(self.c_tot_adj[point]))

            # Calculate species concnetration or each curve point
            species_conc_calc = self._newtonRaphson(
                point,
                c,
                self.model,
                self.log_beta,
                self.c_tot_adj[point],
                self.nc,
                self.ns,
                self.nf,
            )

            # Store calculated species concentration into a vector
            results_species_conc.append(species_conc_calc)

        # Stack calculated species concentration in tabular fashion (points x species)
        results_species_conc = np.stack(results_species_conc)

        # Return distribution
        return results_species_conc

    def _newtonRaphson(self, point, c, model, log_beta, c_tot, nc, ns, nf):
        # FIXME: FOR DEBUGGING PURPOSES
        np.seterr("print")

        # Initiate the matrix for jacobian
        J = np.zeros(shape=(nc, nc))

        for iteration in range(1000):
            logging.debug(
                "-> BEGINNING ITERATION {} ON POINT {}".format(iteration, point)
            )
            # Calculate total concentration given the species concentration
            c_tot_calc, c_spec = self._speciesConcentration(
                c, model, log_beta, nc, ns, nf
            )

            # Compute difference between total concentrations
            delta = c_tot - c_tot_calc

            # TODO: convergence criteria is sloppy as best
            # conv_criteria = np.sum(np.divide(delta, c_tot) ** 2)
            # logging.debug(

            conv_criteria = np.sum(delta) ** 2

            logging.debug(
                "Convergence at Point {} iteration {}: {}".format(
                    point, iteration, conv_criteria
                )
            )

            if conv_criteria < 1e-15:
                return c_spec

            for j in range(nc):
                for k in range(j, nc):
                    J[j, k] = np.sum(model[j] * model[k] * c_spec)
                    J[k, j] = J[j, k]

            # Calculate shift to free concentration
            delta_c = np.linalg.solve(J, delta) * c

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

            # print((c_tot > 0).all())
            # if (c_tot > 0).all():
            #     c = self._damping(point, c, log_beta, c_tot, model, nc, ns, nf)
            # else:
            #     pass

        else:
            logging.error(
                "Calculation terminated early, no convergence found at point {}".format(
                    point
                )
            )
            # FIXME: for debug purposes this is disabled, needs to be re enabled in prod
            # return c_spec
            # raise Exception(
            #     "Calculation of species concentration aborted, no convergence found with conc {} at point {}".format(
            #         str(c_spec), point
            #     )
            # )

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
        logging.debug("Calculated Total Concentration: {}".format(c_tot_calc))

        return c_tot_calc, c_spec

    # def _damping(self, point, c, log_beta, c_tot, model, nc, ns, nf):
    #     logging.debug("ENTERING DAMP ROUTINE")
    #     # TODO: Dampening of free concentration

    #     c_tot_calc, c_spec = self._speciesConcentration(c, model, log_beta, nc, ns, nf)

    #     ## ES42020 METHOD

    #     clim1 = np.abs(c_tot) / 4
    #     clim2 = np.abs(c_tot) * 4

    #     damp_iteration = 0
    #     while damp_iteration < 1000:
    #         fmin = 1
    #         fmax = 1
    #         for i, calc_c in enumerate(c_tot_calc):
    #             if abs(calc_c) < (clim1[i] / 2) or abs(calc_c) > (clim2[i] / 2):
    #                 fatt = abs(c_tot[i] / calc_c)
    #                 if fatt < fmin:
    #                     m1 = i
    #                     fmin = fatt
    #                 elif fatt > fmax:
    #                     m2 = i
    #                     fmax = fatt
    #                 else:
    #                     pass

    #         if fmin != 1:
    #             fatt = fmin
    #             j = m1
    #         elif fmax != 1:
    #             fatt = fmax
    #             j = m2
    #         else:
    #             logging.debug("EXITING DAMP ROUTINE")
    #             return c

    #         exp = np.max(model[j]) ** (-1 / 1)
    #         logging.debug("Damping {} by a factor {}".format(j, (fatt ** exp)))
    #         c[j] = c[j] * fatt ** exp
    #         logging.debug("Damped C: {}".format(c))
    #         c_tot_calc, c_spec = self._speciesConcentration(
    #             c, model, log_beta, nc, ns, nf
    #         )
    #         if np.isnan(c_tot_calc).any():
    #             raise Exception(
    #                 "Dampening routine got invalid values: {} at point {}".format(
    #                     c, point
    #                 )
    #             )

    #         damp_iteration += 1

    #     ## ARTICLE METHOD
    #     # print(c_tot)
    #     # print(c_tot_calc)
    #     # R = np.abs(np.divide(c_tot, c_tot_calc))
    #     # damp_iteration = 0
    #     # while all((R > 1 / 4) & (R < 4)) != True:
    #     #     if damp_iteration > 1000:
    #     #         raise Exception(
    #     #             "Dampening routine got in a infinite loop: {} at point {}".format(
    #     #                 str(c), point
    #     #             )
    #     #         )
    #     #     R = np.ma.array(R, mask=False)
    #     #     logging.debug("R: {}".format(R))
    #     #     R.mask[(R > 1 / 4) & (R < 4)] = True

    #     #     if any(R < 1):
    #     #         to_damp = np.argmin(R)
    #     #     else:
    #     #         to_damp = np.argmax(R)

    #     #     exp = np.max(model[to_damp]) ** (-1 / 1)
    #     #     logging.debug("exp: {}".format(exp))

    #     #     c[to_damp] = c[to_damp] * (R[to_damp] ** exp)

    #     #     logging.debug("damped c: {}".format(c))

    #     #     c_tot_calc, c_spec = self._speciesConcentration(
    #     #         c, model, log_beta, nc, ns, nf
    #     #     )
    #     #     R = np.abs(np.divide(c_tot, c_tot_calc))
    #     #     damp_iteration = damp_iteration + 1

    #     # return c

    def _speciesNames(self, model, comps):
        """
        Returns species names as brute formula from comp names and coefficients
        """
        model = model.T
        names = []

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
