import math
from pprint import pprint

import numpy as np
import pandas as pd


class Optimizer:
    """
    Optimizazion of parameters using Newton-Gauss-Levenberg/Marquardt method
    and Newton-Raphson method to solve mass balance equations.
    """

    def __init__(self):
        pass

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

        # Electroactive species
        self.comp_pot = data["comp_pot"]
        ph_range = data["ph_range"]  # initial and final pH range

        self.comp_name = data["compModel"]["Name"]
        comp_charge = data["compModel"]["Charge"]  # Charge values of comp
        species_data = data["speciesModel"]  # Data relative to the species
        titration_data = data["titrModel"]  # Data relative to titration
        comp_titration_data = data["titrCompModel"]  # Data relative to

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
        self.c_added = comp_titration_data.iloc[:, 2].to_numpy(dtype="double")

        # Analytical concentration of each components
        # THE VALUE ARE COPIED SINCE THESE WILL BE MODIFIED
        self.c_tot = comp_titration_data.iloc[:, 1].copy().to_numpy(dtype="double")

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
        base_log_beta = species_data.iloc[:, 1].to_numpy(dtype="double")
        self.log_beta = np.concatenate(
            (np.array([0 for i in range(self.nc)]), base_log_beta), axis=0
        )

        # Compose species names from the model
        self.species_names = self._speciesNames(self.model, comp_titration_data.index)

    def predict(self):
        """
        Given the loaded data returns species distribution.
        """
        # Calculate species distribution
        # Return formatted species distribution as a nice table
        final_result = self._residuals()
        self.species_distribution = pd.DataFrame(
            final_result[0],
            index=self.v_added,
            columns=self.species_names,
        ).rename_axis(index="V. Added [ml]", columns="Species Con. [ml/L]")
        self.pot_calc = final_result[1]

        return True

    def distribution(self):
        return self.species_distribution

    def potential(self):
        return self.pot_calc

    def _residuals(self):
        """
        Calculate species distribution.
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
                c = results_species_conc[(point - 1)][: self.nc]
            elif point == 0:
                c = np.multiply(c_tot_adj[0], 0.001)
                c[self.comp_pot] = 10 ** ((self.potential[0] - self.std_pot) / 59.16)

            # If initial guess for concentration is lower then 1e-15
            # make it 1e-15
            # c = np.where(c > 1e-15, c, 1e-15)

            # Calculate species concnetration or each curve point
            species_conc_calc = self._newtonRaphson(
                c, self.model, betas, c_tot_adj[point], self.nc, self.ns
            )

            # Store calculated species concentration into a vector
            results_species_conc.append(species_conc_calc)

        # Stack calculated species concentration in tabular fashion (points x species)
        results_species_conc = np.stack(results_species_conc)

        # Get the concentration for each point of the electroactive component
        electroactive_conc = results_species_conc[:, self.comp_pot]

        # Calculate predicted potential
        pot_calc = np.array(
            [
                self.std_pot + 59.16 * math.log10(electroactive_conc[i])
                for i in range(self.nop)
            ]
        )

        # Return distribution
        return [results_species_conc, pot_calc]

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
                R = np.ma.array(R, mask=False)
                R.mask[(R > 1 / 10) & (R < 10)] = True
                lnR = np.log(np.abs(R))

                to_damp = np.argmax(lnR)
                exp = np.max(np.abs(model[to_damp])) ** (-1 / 1)

                c[to_damp] = c[to_damp] * (R[to_damp] ** exp)
                c_tot_calc, c_spec = self._speciesConcentration(c, model, betas, nc, ns)

                R = np.divide(c_tot, c_tot_calc)
                damp_iteration = damp_iteration + 1

            # Compute difference between total concentrations
            delta = c_tot - c_tot_calc

            # TODO: convergence criteria
            conv_criteria = sum(np.divide(delta, c_tot) ** 2)
            if conv_criteria < 1e-15:
                return c_spec
            # if all(abs(i) < 1e-15 for i in delta):
            #     return c_spec, J

            for j in range(nc):
                for k in range(j, nc):
                    J[j, k] = sum(model[j] * model[k] * c_spec)
                    J[k, j] = J[j, k]

            # Calculate and apply shift to free concentration
            delta_c = np.linalg.solve(J, delta) * c
            c = c + delta_c

            # If any concentration is negative go back half a shift
            # Break out of the loop if all shifts are approx. zero
            while any(c <= 0):
                delta_c = 0.5 * delta_c
                c = c - delta_c
                if all(abs(i) < 1e-15 for i in delta_c):
                    break

        else:
            raise Exception(
                "Calculation of species concentration aborted, no convergence found with conc %s"
                % str(c_spec)
            )

    # TODO: document added functions
    def _speciesConcentration(self, c, model, betas, nc, ns):
        # Calculate species concentration (c_spec[0->nc]=free conc/c_spec[nc+1->nc+ns]=species conc)
        log_b = np.log10(betas)
        log_c = np.log10(c)
        tiled_c = np.tile(log_c, [ns + nc, 1]).T
        spec_mat = tiled_c * model
        c_spec = np.sum(spec_mat, axis=0) + log_b
        c_spec = 10 ** c_spec
        # c_spec = np.exp(c_spec)

        # c_spec = np.where(c_spec > 1e-15, c_spec, 1e-15)
        # Estimate total concentration given the species concentration
        # print((np.abs(model) * np.tile(c_spec, [nc, 1])))
        c_tot_calc = np.sum((np.abs(model) * np.tile(c_spec, [nc, 1])), axis=1)
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
