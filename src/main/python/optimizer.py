import math
from pprint import pprint

import numpy as np
import pandas as pd


class Optimizer:
    """
    Optimizazion of parameters using Newton-Gauss-Levenberg/Marquardt method
    and Newton-Raphson method to solve mass balance equations.
    """

    def __init__(
        self,
        mu: float = 1e-4,
        delta: float = 1e-10,
        max_it: int = 100,
    ):
        """
        Loads the data from the input to be used in the optimizazion process.

        :param mu: convergence limit.
        :param delta: step size for numerical difference.
        :param max_it: maximum number of iterations.
        """
        self.mu = mu
        self.delta = delta
        self.max_it = max_it

    def fit(self, data):
        """
        Loads the data used to optimize the system.

        :param data: data as given from the GUI.
        """
        # Import number of comp/species
        self.nc = data["nc"]
        self.ns = data["ns"]

        # Number of components and number of species has to be > 0
        if self.nc <= 0 | self.ns <= 0:
            raise Exception(
                "Number of components and number of species have to be > 0."
            )

        # Imports electrode std potential
        self.std_pot = data["std_pot"]

        # SD on potential
        self.sd_e = data["se"]

        # Electro active species
        self.comp_pot = data["comp_pot"]
        ph_range = data["ph_range"]  # initial and final pH range

        self.comp_name = data["compModel"]["Name"]
        comp_charge = data["compModel"]["Charge"]  # Charge values of comp
        species_data = data["speciesModel"]  # Data relative to the species
        titration_data = data["tritModel"]  # Data relative to titration
        comp_tritation_data = data["tritCompModel"]  # Data relative to

        # Check that charge of electroactive component isn't zero.
        if comp_charge[self.comp_pot] == 0:
            raise Exception("Charge of the electroactive component can't be Zero.")

        # Convert ph range to potential range
        pot_range = np.array(
            [
                self.std_pot
                + (59.16 / comp_charge[self.comp_pot]) * math.log10(10 ** -ph_range[i])
                for i in range(2)
            ]
        )

        # Subset the data only taking in account points in the pot_range
        self.v_added, self.potential = self._subsetData(pot_range, titration_data)

        self.nop = len(self.v_added)  # Number of effective points to be used

        # Check if the number of points in the range of pH is greater then 0
        if self.nop == 0:
            raise Exception(
                "Number of titration points in the selected pH range is 0, please pick a wider range."
            )

        # Concentration in the titrant for each component
        self.c_added = comp_tritation_data.iloc[:, 2].to_numpy(dtype="float")

        # Analytical concentration of each components
        # THE VALUE ARE COPIED SINCE THESE WILL BE MODIFIED
        self.c_tot = comp_tritation_data.iloc[:, 1].copy().to_numpy(dtype="float")

        # Initial volume and total volume at each point
        self.v0 = data["v0"]
        self.v_tot = self.v0 + self.v_added

        # SD on volume
        self.sd_v = data["sv"]

        # Define the stechiometric coefficients for the various species
        # IMPORTANT: each component is considered as a species with logB = 0
        aux_model = np.identity(self.nc, dtype="int")
        base_model = species_data.iloc[:, 2:].to_numpy(dtype="int").T
        self.model = np.concatenate((aux_model, base_model), axis=1)

        # Stores log_betas
        base_log_beta = species_data.iloc[:, 1].to_numpy(dtype="float")
        self.log_beta = np.concatenate(
            (np.array([0 for i in range(self.nc)]), base_log_beta), axis=0
        )

        # Stores array with info on which betas to optimize and int with number
        # comp_flags is used since the array containing the betas alsoof params
        # include elements for the components which don't need to be
        # touched by the optimization routine
        comp_flags = np.array([False for i in range(self.nc)])
        species_flags = species_data.iloc[:, 0].to_numpy(dtype="bool")
        self.b_to_opt = np.append(comp_flags, species_flags)

        # Stores array with info on which analytical concentrations to optimize
        self.c_to_opt = comp_tritation_data.iloc[:, 0].to_numpy(dtype="bool")

        # Total number of parameters to optimize =
        # number of variable betas + variable C0s
        self.num_opt = sum(species_flags) + sum(self.c_to_opt)

        # Compose species names from the model
        self.species_names = self._speciesNames(self.model, comp_tritation_data.index)

        # Flag indicating if the optimization is weighted or not
        self.wmode = data["wmode"]
        # TODO: import sd_e/sd_v only if wmode != 0

        # Check, if wmode is 1, that sd_e/sd_v aren't zero
        if self.wmode == 1:
            if self.sd_v == 0 or self.sd_e == 0:
                raise Exception(
                    "The weighted optimization routine requires walues for the SD of volume and potential to be different from 0!"
                )

    def predict(self):
        """
        Given the loaded data returns the parameters values after each iteration,
        species concentration at the end of the process and the corresponding potential.
        """
        txt_output = []

        # calculate weights for each experimental point
        # if wmode is 0 work with unitary weights.
        weights = self._weights(self.nop, self.sd_v, self.sd_e, self.wmode)

        # If no param is flagged to be optimized skip everything
        # and just calculate species distribution
        if self.num_opt != 0:
            # Initialize Marquardt param and fixes ssq_old as arbitrary high value
            mp = 0
            ssq_old = 1e50
            # Design matrix as (number points x number param to optimize)
            J = np.zeros(shape=(self.nop, self.num_opt))

            # Iterative opt cycle with max number of iteration
            for it in range(self.max_it):
                print("iternation number %i" % it)

                # Calculate residuals from experimental curve
                r0, design, species = self._residuals()

                # Compute weighted sum of squares and convergence check
                ssq = r0.T @ weights @ r0
                conv_crit = (ssq_old - ssq) / ssq_old

                # Check convergence
                if abs(conv_crit) <= self.mu:  # Min reached
                    print("min", "--", mp)
                    if mp == 0:
                        # Return succesful termination
                        break
                    else:
                        # If mp wasn't zero put it to zero
                        mp = 0
                        # Store current residuals as old
                        r0_old = r0
                elif conv_crit > self.mu:  # Convergence
                    print("converging", "--", mp)
                    # If converging reduce mp
                    mp = mp / 3
                    # Store current ssq and residuals as old
                    ssq_old = ssq
                    r0_old = r0

                    # Estimate derviative of potential with respect to the param to opt
                    # TODO: this is the crudest form I could think of doing it, there has to be a better way!!
                    param_count = 0
                    for i, flag in enumerate(self.b_to_opt):
                        if flag:
                            # for j in range(self.nop):
                            #     y = [-species[j, i], -species[j, i]]
                            #     J[j, param_count] = np.linalg.solve(design[j], y)[
                            #         self.comp_pot
                            #     ] / (10 ** self.log_beta[i])
                            self.log_beta[i] = self.log_beta[i] * (1 + self.delta)
                            print("!!!EXTIMATHING DERIVATIVE!!!")
                            r, _, _ = self._residuals()
                            print("!!!FINISHED EXHTIMATING DERIVATIVE!!!")
                            self.log_beta[i] = self.log_beta[i] / (1 + self.delta)
                            J[:, param_count] = np.reshape(
                                (r - r0) / (self.delta * self.log_beta[i]), self.nop
                            )
                            param_count += 1
                    for i, flag in enumerate(self.c_to_opt):
                        if flag:
                            self.c_tot[i] = self.c_tot[i] * (1 + self.delta)
                            r, _, _ = self._residuals()
                            self.c_tot[i] = self.c_tot[i] / (1 + self.delta)
                            J[:, param_count] = np.reshape(
                                (r - r0) / (self.delta * self.c_tot[i]), self.nop
                            )
                            param_count += 1

                elif conv_crit < -self.mu:  # Divergence
                    print("diverging", "--", mp)
                    # If diverging augment the mp value
                    if mp == 0:
                        mp = 1
                    else:
                        mp = mp * 5

                    # Put back the param to opt of the applied shift (since it was too much)
                    param_count = 0
                    for i, flag in enumerate(self.b_to_opt):
                        if flag:
                            self.log_beta[i] = self.log_beta[i] - delta_p[param_count]
                            param_count += 1
                    for i, flag in enumerate(self.c_to_opt):
                        if flag:
                            self.c_tot[i] = self.c_tot[i] - delta_p[param_count]
                            param_count += 1

                # Calculate Sigma from the Curvature Matrix
                curv_matrix = np.linalg.pinv(J.T @ weights @ J)
                sigma = math.sqrt(ssq / (self.nop - self.num_opt))
                # Estimate error for each param to opt
                param_sigma = sigma * np.sqrt(np.diagonal(curv_matrix))
                # print(J)
                # Compute the param shift
                delta_p = -(
                    np.linalg.pinv(J.T @ weights @ J + np.identity(self.num_opt) * mp)
                    @ (J.T @ weights)
                    @ r0_old
                )

                # Store the iteration results as text that will be output to the user
                txt_output.append("Iteration N° %i" % int(it + 1))
                txt_output.append("Sigma = %f" % float(sigma))

                param_count = 0
                for i, flag in enumerate(self.b_to_opt):
                    if flag:
                        self.log_beta[i] = self.log_beta[i] + delta_p[param_count]
                        txt_output.append(
                            "".join(
                                [
                                    "\t",
                                    "LogB",
                                    "\t",
                                    str(self.species_names[i]),
                                    "\t",
                                    "--- ",
                                    str(self.log_beta[i]),
                                    " ± ",
                                    str(param_sigma[param_count]),
                                ]
                            )
                        )
                        param_count += 1

                for i, flag in enumerate(self.c_to_opt):
                    if flag:
                        self.c_tot[i] = self.c_tot[i] + delta_p[param_count]
                        # print(self.c_tot[i])
                        txt_output.append(
                            "".join(
                                [
                                    "\t",
                                    "C0",
                                    "\t",
                                    str(self.comp_name[i]),
                                    "\t",
                                    "--- ",
                                    str(self.c_tot[i]),
                                    " ± ",
                                    str(param_sigma[param_count]),
                                ]
                            )
                        )
                        param_count += 1

            else:
                raise Exception(
                    "Max iteration reached while optimizing parameters, no convergence found for the system."
                )
        else:
            txt_output.append(
                "No parameters selected for optimization! Calculating species distribution."
            )

        # Calculate species distribution with optimized params
        # Return formatted species distribution as a nice table
        final_result = self._residuals(distribution=True)
        species_distribution = pd.DataFrame(
            final_result[0],
            index=self.v_added,
            columns=self.species_names,
        ).rename_axis(index="V. Added [ml]", columns="Species Con. [ml/L]")
        pot_calc = final_result[1]

        return [txt_output, species_distribution, pot_calc]

    def _residuals(self, distribution=False):
        """
        Calculate the residuals given the model and the analytical results,
        it can also output the species distribution
        when the optimization routine is done
        """

        # Calculate betas from LogBetas
        betas = 10 ** self.log_beta
        # Initialize array to contain the species concentration
        # obtained from the calculations
        results_species_conc = []

        results_der = []

        # Total concentration corrected for v_tot
        c_tot_adj = (
            np.tile(self.c_tot, [self.nop, 1]) * self.v0
            + np.tile(self.v_added, [self.nc, 1]).T * self.c_added
        ) / np.tile(self.v_tot, [self.nc, 1]).T

        # Cycle over each point of titration
        for point in range(self.nop):
            print("point: ", point)

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
            elif point > 0:
                # Concentration of components to be used in the next iteration
                c = results_species_conc[(point - 1)][: self.nc]
            elif point == 0:
                c = np.multiply(c_tot_adj[0], 0.001)
                c[self.comp_pot] = 10 ** ((self.potential[0] - self.std_pot) / 59.16)
                print("Point Zero initial guess: ", c)

            # If initial guess for concentration is lower then 1e-15
            # make it 1e-15
            # c = np.where(c > 1e-15, c, 1e-15)

            # Calculate species concnetration or each curve point
            species_conc_calc, der = self._newtonRaphson(
                c, self.model, betas, c_tot_adj[point], self.nc, self.ns
            )

            # Store calculated species concentration into a vector
            results_species_conc.append(species_conc_calc)
            results_der.append(der)

        # Stack calculated species concentration in tabular fashion (points x species)
        results_species_conc = np.stack(results_species_conc)

        results_der = np.stack(results_der)

        # Get the concentration for each point of the electroactive component
        electroactive_conc = results_species_conc[:, self.comp_pot]

        # Calculate predicted potential
        pot_calc = np.array(
            [
                self.std_pot + 59.16 * math.log10(electroactive_conc[i])
                for i in range(self.nop)
            ]
        )

        # Return the desired info (distribution or just residuals)
        if distribution:
            return [results_species_conc, pot_calc]
        else:
            # Calculate residuals from real curve
            # Return a column vector for further calculations
            residuals = self.potential - pot_calc
            residuals = residuals[:, np.newaxis]
            return residuals, results_der, results_species_conc

    def _newtonRaphson(self, c, model, betas, c_tot, nc, ns):
        # FIXME: FOR DEBUGGING PURPOSES
        np.seterr("raise")

        # Initiate the matrix for jacobian
        J = np.zeros(shape=(nc, nc))

        for iteration in range(100):
            # Calculate total concentration given the species concentration
            c_tot_calc, c_spec = self._speciesConcentration(c, model, betas, nc, ns)

            # TODO: Dampening of free concentration
            R = np.divide(c_tot, c_tot_calc)
            damp_iteration = 0
            while all((R > 1 / 10) & (R < 10)) != True:
                if damp_iteration > 100:
                    raise Exception(
                        "Dampening routine got in a infinite loop: %s" % str(c)
                    )
                # print("before:", R)
                R = np.ma.array(R, mask=False)
                R.mask[(R > 1 / 10) & (R < 10)] = True
                lnR = np.log(np.abs(R))

                # print("masked: ", lnR)
                to_damp = np.argmax(lnR)
                print("coefficient for K comp: ", model[to_damp])
                exp = np.max(np.abs(model[to_damp])) ** (-1 / 1)
                # print("exp:", exp)

                # print("got here")
                c[to_damp] = c[to_damp] * (R[to_damp] ** exp)
                # c[to_damp] = 10 ** (np.log10(c[to_damp]) + exp * np.log10(R[to_damp]))
                print("damped c: ", c, "\n Rates: ", R, "\n lnRates: ", lnR)
                # c = np.where(c > 1e-15, c, 1e-15)
                c_tot_calc, c_spec = self._speciesConcentration(c, model, betas, nc, ns)

                R = np.divide(c_tot, c_tot_calc)
                # print("after:", R)
                # print("conc: ", c)
                damp_iteration = damp_iteration + 1

            # Compute difference between total concentrations
            delta = c_tot - c_tot_calc

            # TODO: convergence criteria
            conv_criteria = sum(np.divide(delta, c_tot) ** 2)
            if conv_criteria < 1e-15:
                return c_spec, J
            # if all(abs(i) < 1e-15 for i in delta):
            #     return c_spec, J

            for j in range(nc):
                for k in range(j, nc):
                    J[j, k] = sum(model[j] * model[k] * c_spec)
                    J[k, j] = J[j, k]

            # Calculate and apply shift to free concentration
            delta_c = np.linalg.solve(J, delta) * c
            c = c + delta_c
            print("Updated c: ", c)

            # If any concentration is negative go back half a shift
            # Break out of the loop if all shifts are approx. zero
            while any(c <= 0):
                delta_c = 0.5 * delta_c
                c = c - delta_c
                print("Positivizing C: ", c)
                if all(abs(i) < 1e-15 for i in delta_c):
                    c = np.where(c > 1e-15, c, 1e-15)
                    print("failed positivizing: ", c)
                    break

        else:
            raise Exception(
                "Calculation of species concentration aborted, no convergence found with conc %s"
                % str(c_spec)
            )

    # TODO: document added functions
    def _speciesConcentration(self, c, model, betas, nc, ns):
        # Calculate species concentration (c_spec[0->nc]=free conc/c_spec[nc+1->nc+ns]=species conc)
        # print("Guess: ", c)
        log_b = np.log10(betas)
        log_c = np.log10(c)
        tiled_c = np.tile(log_c, [ns + nc, 1]).T
        spec_mat = tiled_c * model
        c_spec = np.sum(spec_mat, axis=0) + log_b
        c_spec = 10 ** c_spec
        #c_spec = np.exp(c_spec)
        
        # c_spec = np.where(c_spec > 1e-15, c_spec, 1e-15)
        # Estimate total concentration given the species concentration
        # print((np.abs(model) * np.tile(c_spec, [nc, 1])))
        c_tot_calc = np.sum((np.abs(model) * np.tile(c_spec, [nc, 1])), axis=1)
        print("c_tot_c ", c_tot_calc)
        # c_tot_calc = np.where(c_tot_calc > 1e-15, c_tot_calc, 1e-15)

        # print("result: ", c_tot_calc)
        return c_tot_calc, c_spec

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

    def _weights(self, nop, sv, se, wmode):
        """
        Calculate weights from titration curve and deviation of volume and potential.
        If wmode = 0 then weight matrix == I[nop,nop]

        :param nop: number of experimental points.
        :param sv: standard deviation volume.
        :param se: standard deviation potential.
        :param wmode: whether to use equal weights or calculated ones for every point.
        """
        if wmode == 1:
            # Calculate gradient of experimental titration curve
            der = np.gradient(self.potential, self.v_added)
            # Define s² as SD_e² + der² x SD_v²
            s2 = (se * se) + (der * der) * (sv * sv)
            # Weight vector as reciprocal of s2
            weights = np.reciprocal(s2)
            # Weight matrix is a diagonal one
            matrix_weights = np.diag(weights)
        else:
            # If working with unitary weights return an identity matrix
            matrix_weights = np.identity(self.nop)

        return matrix_weights

    def _subsetData(self, pot_range, titration_data):
        """
        Given the potential range and the titration data
        subset the latter to the desired first range.
        """
        # Lower limit is the lowest value in potential
        # Higher limit is the highest
        ll = pot_range.min()
        hl = pot_range.max()
        # If either lowe/higher is lowe or higher then the lowest value present
        # use that as ll/hl
        if ll < titration_data["Potential"].min():
            ll = titration_data["Potential"].min()
        if hl > titration_data["Potential"].max():
            hl = titration_data["Potential"].max()

        # subset of Volume of titrant added, return numpy array
        v_added = titration_data[
            (titration_data["Potential"] >= ll) & (titration_data["Potential"] <= hl)
        ]["Volume"].to_numpy()
        # subset of Analytical potential values, return numpy array
        potential = titration_data[
            (titration_data["Potential"] >= ll) & (titration_data["Potential"] <= hl)
        ]["Potential"].to_numpy()

        return v_added, potential
