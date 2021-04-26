import math
import logging
from pprint import pprint

import numpy as np
import pandas as pd
from scipy.special import logsumexp
from scipy.optimize import root


class Optimizer:
    """
    Optimizazion of parameters using Newton-Gauss-Levenberg/Marquardt method
    and Newton-Raphson method to solve mass balance equations.
    """

    def __init__(self):
        self.epsl = 200

    def fit(self, data):
        """
        Loads the data used to optimize the system.

        :param data: data as given from the GUI.
        """
        logging.info("--- START DATA LOADING ---")
        # Import number of comp/species/phases
        self.nc = data["nc"]
        self.ns = data["ns"]
        self.nf = data["np"]

        # Number of components and number of species has to be > 0
        if self.nc <= 0 | (self.ns <= 0 & self.nf <= 0):
            raise Exception(
                "Number of components and number of species have to be > 0."
            )

        self.comp_name = data["compModel"]["Name"]
        # Charge values of comps
        self.comp_charge = data["compModel"]["Charge"]
        # Data relative to the species and solis species
        self.species_data = data["speciesModel"]
        self.solid_species_data = data["solidSpeciesModel"]
        # Data relative to comp concentrations
        self.conc_data = data["concModel"]

        # Analytical concentration of each component
        self.c_tot = self.conc_data.iloc[:, 0].copy().to_numpy(dtype="float")

        # Concentration in the titrant for each component
        self.c_added = self.conc_data.iloc[:, 1].to_numpy(dtype="float")

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
            raise Exception("Number of points in the titration is 0.print")

        self.v_added = []
        for x in range(self.nop):
            self.v_added.append(self.vinc * x)
        self.v_added = np.array(self.v_added)
        v1_diff = self.initv - self.v0
        self.v_added += v1_diff
        self.v_tot = self.v0 + self.v_added

        # Total concentration corrected for v_tot
        self.c_tot_adj = (
            np.tile(self.c_tot, [self.nop, 1]) * self.v0
            + np.tile(self.v_added, [self.nc, 1]).T * self.c_added
        ) / np.tile(self.v_tot, [self.nc, 1]).T

        # Define the stechiometric coefficients for the various species
        # IMPORTANT: each component is considered as a species with logB = 0
        aux_model = np.identity(self.nc, dtype="int")
        base_model = self.species_data.iloc[:, 6:].to_numpy(dtype="int").T
        self.model = np.concatenate((aux_model, base_model), axis=1)

        # Stores log_betas
        base_log_beta = self.species_data.iloc[:, 0].to_numpy(dtype="float")
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
        logging.info("--- START CALCULATION --- ")
        final_result = self._residuals()
        self.species_distribution = pd.DataFrame(
            final_result,
            index=self.v_added,
            columns=self.species_names,
        ).rename_axis(index="V. Added [ml]", columns="Species Con. [ml/L]")
        logging.info("--- CALCULATION TERMINATED ---")

        return True

    def distribution(self):
        return self.species_distribution

    def potential(self):
        return self.pot_calc

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
                v = self.v_added[point]
                v1 = self.v_added[(point - 1)]
                v2 = self.v_added[(point - 2)]
                v3 = self.v_added[(point - 3)]
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

        for iteration in range(200):
            logging.debug("-> Iteration {} for point {}".format(iteration, point))
            # Calculate total concentration given the species concentration
            c_tot_calc, c_spec = self._speciesConcentration(
                c, model, log_beta, nc, ns, nf
            )

            # Compute difference between total concentrations
            delta = c_tot - c_tot_calc

            # TODO: convergence criteria
            conv_criteria = np.sum(np.divide(delta, c_tot) ** 2)
            logging.debug(
                "ConvergenceC. at Point {} iteration {}: {}".format(
                    point, iteration, conv_criteria
                )
            )
            if conv_criteria < 1e-10:
                return c_spec

            for j in range(nc):
                for k in range(j, nc):
                    J[j, k] = np.sum(model[j] * model[k] * c_spec)
                    J[k, j] = J[j, k]

            # Calculate and apply shift to free concentration
            delta_c = np.linalg.solve(J, delta) * c

            # Positive constrain on freeC as present in STACO
            for i, shift in enumerate(delta_c):
                if shift <= -c[i]:
                    logging.debug("positivizing on comp: {}".format(i))
                    factor = -0.99 * c[i] / shift
                    delta_c = factor * delta_c

            c = c + delta_c
            logging.debug("N-R updated freeC: {}".format(c))

            c = self._damping(point, c, log_beta, c_tot, model, nc, ns, nf)

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
        logging.debug("cspec: {}".format(c_spec))

        # Estimate total concentration given the species concentration
        c_tot_calc = np.sum(model * np.tile(c_spec, [nc, 1]), axis=1)
        logging.debug("c_tot_calc: {}".format(c_tot_calc))

        return c_tot_calc, c_spec

    def _damping(self, point, c, log_beta, c_tot, model, nc, ns, nf):
        logging.debug("Entering damp routine")
        # TODO: Dampening of free concentration

        c_tot_calc, c_spec = self._speciesConcentration(c, model, log_beta, nc, ns, nf)
        R = np.abs(np.divide(c_tot, c_tot_calc))
        damp_iteration = 0
        while all((R > 1 / 4) & (R < 4)) != True:
            if damp_iteration > 1000:
                raise Exception(
                    "Dampening routine got in a infinite loop: {} at point {}".format(
                        str(c), point
                    )
                )
            R = np.ma.array(R, mask=False)
            logging.debug("R: {}".format(R))
            R.mask[(R > 1 / 4) & (R < 4)] = True

            if any(R < 1):
                to_damp = np.argmin(R)
            else:
                to_damp = np.argmax(R)

            exp = np.max(model[to_damp]) ** (-1 / 1)
            logging.debug("exp: {}".format(exp))

            c[to_damp] = c[to_damp] * (R[to_damp] ** exp)

            logging.debug("damped c: {}".format(c))

            c_tot_calc, c_spec = self._speciesConcentration(
                c, model, log_beta, nc, ns, nf
            )
            R = np.abs(np.divide(c_tot, c_tot_calc))
            damp_iteration = damp_iteration + 1

        return c

    def _speciesNames(self, model, comps):
        """
        Returns species names as brute formula from comp names and coefficients
        """
        model = model.T
        names = []

        for i in range(len(model)):
            names.append("")
            for j, comp in enumerate(comps):
                names[i] = names[i] + ("(" + comp + ")") * (
                    1 if model[i][j] != 0 else 0
                )
                if model[i][j] >= 2 or model[i][j] < 0:
                    names[i] = names[i] + str(model[i][j])
                else:
                    pass

        return names