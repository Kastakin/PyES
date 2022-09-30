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
        # Titration or Distribution mode
        if data["dmode"] == 0:
            self.distribution = False
        else:
            self.distribution = True

        if data["emode"] == 0:
            self.errors = True
        else:
            self.errors = False

        # Charge values of comps
        self.comp_charge = pd.DataFrame(data["compModel"])["Charge"]
        # Data relative to the species and solid species
        self.species_data: pd.DataFrame = pd.DataFrame(data["speciesModel"])
        self.solid_data: pd.DataFrame = pd.DataFrame(data["solidSpeciesModel"])
        # Data relative to comp concentrations
        self.conc_data = pd.DataFrame(data["concModel"])

        if self.distribution:
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
            self.ind_comp_logs = np.arange(
                self.initl, (self.finall + self.linc), self.linc
            )
            self.ind_comp_c = 10 ** (-self.ind_comp_logs)

            # Calculate the number of points in the interval
            self.nop = len(self.ind_comp_c)
        else:
            self.c_added = self.conc_data.iloc[:, 1].copy().to_numpy(dtype="float")
            # Initial volume
            self.v0 = data["v0"] * 1e-3
            # First titration point volume
            self.initv = data["initv"] * 1e-3
            # Volume increment at each point
            self.vinc = data["vinc"] * 1e-3
            # number of points
            self.nop = int(data["nop"])

            if self.v0 <= 0:
                raise Exception("Initial volume can't be zero")

            if self.vinc <= 0:
                raise Exception("Volume increments should be higher then 0.")

            if self.v0 > self.initv:
                raise Exception(
                    "Initial titration volume should be higer or equal to initial volume."
                )

            self.v_added = np.array([self.vinc * x for x in range(self.nop)])
            v1_diff = self.initv - self.v0
            self.v_added += v1_diff
            self.v_tot = self.v0 + self.v_added

        # Check if the number of points in the range of pH is greater then 0
        if self.nop == 0:
            raise Exception("Number of points in the -log[A] range shouldn't be 0.")

        # Analytical concentration of each component (including the ones that will be ignored)
        self.c_tot = self.conc_data.iloc[:, 0].copy().to_numpy(dtype="float")

        if self.distribution:
            self.c_tot = np.delete(self.c_tot, self.ind_comp, 0)

        # Check if thay are all zero
        if (self.c_tot == 0).all():
            raise Exception(
                "Analytical concentration shouldn't be zero for all components."
            )

        # Charges of components
        self.comp_charge = self.comp_charge.copy().to_numpy(dtype="int")

        # Find which components have to be ignored (c0 = 0)
        ignored_comps = np.where(self.c_tot == 0)[0]

        # Remove the concentration and charge data relative to those
        self.c_tot = np.delete(self.c_tot, ignored_comps, 0)
        self.comp_charge = np.delete(self.comp_charge, ignored_comps)

        # get number of effective components
        self.nc = int(len(self.conc_data)) - len(ignored_comps)

        if self.distribution:
            # for every ignored comp which index is lower
            # of the designated indipendent comp
            # reduce its index by one (they "slide over")
            self.ind_comp = self.ind_comp - (ignored_comps < self.ind_comp).sum()
            # Assign total concentrations for each point
            self.c_tot = np.tile(self.c_tot, [self.nop, 1])
        else:
            self.initial_c = self.c_tot
            self.c_tot = (
                (np.tile(self.c_tot, [self.nop, 1]) * self.v0)
                + (np.tile(self.v_added, [self.nc, 1]).T * self.c_added)
            ) / (np.tile(self.v_tot, [self.nc, 1]).T)

        # Store the stechiometric coefficients for the components
        # IMPORTANT: each component is considered as a species with logB = 0
        comp_model = np.identity(self.nc, dtype="int")

        # Ignore the rows relative to the flagged as ignored species and ignored solid species
        species_not_ignored = self.species_data.loc[
            self.species_data["Ignored"] == False
        ]
        solid_not_ignored = self.solid_data.loc[self.solid_data["Ignored"] == False]

        species_duplicates = species_not_ignored.loc[
            species_not_ignored.duplicated(subset="Name", keep="first").to_list(),
            "Name",
        ]
        if not species_duplicates.empty:
            raise Exception(
                f"Species {', '.join(species_duplicates.to_list())} with indices {', '.join(species_duplicates.index.astype(str).to_list())} appear to be duplicates, you can and should remove them to avoid ambiguities in the results."
            )

        solids_duplicates = solid_not_ignored.loc[
            solid_not_ignored.duplicated(subset="Name", keep="first").to_list(),
            "Name",
        ]
        if not solids_duplicates.empty:
            raise Exception(
                f"Solids {', '.join(solids_duplicates.to_list())} with indices {', '.join(solids_duplicates.index.astype(str).to_list())} appear to be duplicates, you can and should remove them to avoid ambiguities in the results."
            )

        # Store the stechiometric coefficients for the species and solid species
        base_model = species_not_ignored.iloc[:, 8:-1].to_numpy(dtype="int").T
        solid_model = solid_not_ignored.iloc[:, 8:-1].to_numpy(dtype="int").T

        # Stores log_betas and log_ks of not ignored species
        base_log_beta = species_not_ignored.iloc[:, 2].to_numpy(dtype="float")
        base_log_ks = solid_not_ignored.iloc[:, 2].to_numpy(dtype="float")

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
        base_log_ks = np.delete(base_log_ks, solid_to_remove, axis=0)
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
        self.species_perc_int, self.solid_perc_int = self._percEncoder(
            ignored_comp_names
        )

        # Assemble the models and betas matrix
        self.model = np.concatenate((comp_model, base_model), axis=1)
        self.log_beta_ris = np.concatenate(
            (np.array([0 for i in range(self.nc)]), base_log_beta), axis=0
        )
        self.solid_model = solid_model
        self.log_ks_ris = base_log_ks

        # Get the number of not-ignored species/solid species
        self.ns = base_model.shape[1]
        self.nf = solid_model.shape[1]

        # Number of components and number of species/solids has to be > 0
        if self.nc <= 0 | (self.ns <= 0 & self.nf <= 0):
            raise Exception(
                "Number of components and number of not ignored species should be more then zero."
            )

        if self.errors:
            self.c0_sigma = self.conc_data.iloc[:, 2].copy().to_numpy(dtype="float")
            self.c0_sigma = np.delete(self.c0_sigma, ignored_comps)
            if self.distribution:
                self.c0_sigma[self.ind_comp] = 0
                self.conc_sigma = np.tile(self.c0_sigma, [self.nop, 1])
            else:
                self.ct_sigma = self.conc_data.iloc[:, 3].copy().to_numpy(dtype="float")
                self.ct_sigma = np.delete(self.ct_sigma, ignored_comps)
                self.conc_sigma = np.tile(self.c0_sigma, [self.nop, 1]) + (
                    np.tile(self.v_added, [self.nc, 1]).T * self.ct_sigma
                )

            self.log_beta_sigma = species_not_ignored.iloc[:, 3].to_numpy(dtype="float")
            self.log_ks_sigma = solid_not_ignored.iloc[:, 3].to_numpy(dtype="float")

            self.log_beta_sigma = np.delete(
                self.log_beta_sigma, species_to_remove, axis=0
            )
            self.log_ks_sigma = np.delete(self.log_ks_sigma, solid_to_remove, axis=0)

            self.beta_sigma = (
                self.log_beta_sigma * np.log(10) * (10 ** self.log_beta_ris[self.nc :])
            )

            self.ks_sigma = self.log_ks_sigma * np.log(10) * (10**self.log_ks_ris)

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

            # If ref. ionic strength is not given for one of the species use the reference one
            self.species_ris = np.where(
                self.species_ris == 0, data["ris"], self.species_ris
            )
            self.solid_ris = np.where(self.solid_ris == 0, data["ris"], self.solid_ris)

            # Add ref. ionic strength for components
            self.species_ris = np.insert(
                self.species_ris, 0, [data["ris"] for i in range(self.nc)]
            )
            # Calculate square root of reference ionic strength for species
            self.species_radqris = np.sqrt(self.species_ris)
            self.solid_radqris = np.sqrt(self.solid_ris)

            # Load background ions concentration
            if self.distribution:
                self.background_c = np.tile(data["cback"], self.nop)
            else:
                background_c0 = data["c0back"]
                background_ct = data["ctback"]
                self.background_c = np.array(
                    ((background_c0 * self.v0) + (background_ct * self.v_added))
                    / self.v_tot
                )

            a = data["a"]
            self.b = data["b"]
            c = [data["c0"], data["c1"]]
            d = [data["d0"], data["d1"]]
            e = [data["e0"], data["e1"]]

            # Check if default have to be used
            if (a == 0) & (self.b == 0):
                a = 0.5
                self.b = 1.5

            # Compute p* for alla the species
            species_past = self.model.sum(axis=0) - 1
            solid_past = self.solid_model.sum(axis=0)

            # Reshape charges into a column vector
            comp_charge_column = np.reshape(self.comp_charge, (self.nc, 1))

            if self.distribution:
                # Same vector except missing the charge of the indipendent component, used later in the computation
                self.comp_charge_no_indipendent = np.delete(
                    self.comp_charge, self.ind_comp
                )

            # Compute species charges
            self.species_charges = (self.model * comp_charge_column).sum(axis=0)
            self.solid_charges = (self.solid_model * comp_charge_column).sum(axis=0)

            # Compute z* for all the species
            species_zast = (self.model * (comp_charge_column**2)).sum(axis=0) - (
                self.species_charges
            ) ** 2
            solid_zast = (self.solid_model * (comp_charge_column**2)).sum(axis=0)

            # Compute A/B term of D-H equation
            self.species_az = a * species_zast
            self.solid_az = a * solid_zast

            self.species_fib = self.species_radqris / (
                1 + (self.b * self.species_radqris)
            )
            self.solid_fib = self.solid_radqris / (1 + (self.b * self.solid_radqris))

            # For both species and solids sets the Debye-Huckle parameters used to update their defining constants
            (self.species_cg, self.species_dg, self.species_eg) = self._setBHParams(
                species_not_ignored,
                species_to_remove,
                species_past,
                species_zast,
                c,
                d,
                e,
            )

            (self.solid_cg, self.solid_dg, self.solid_eg) = self._setBHParams(
                solid_not_ignored,
                solid_to_remove,
                solid_past,
                solid_zast,
                c,
                d,
                e,
                solids=True,
            )

        # Compose species names from the model
        self.species_names = self._speciesNames(self.model)
        self.solid_names = self._speciesNames(self.solid_model)
        logging.info("--- DATA LOADED ---")

    def predict(self):
        """
        Given the loaded data returns species distribution.
        """
        # Calculate species distribution
        # Return formatted species distribution as a nice table
        logging.info("--- BEGINNING CALCULATION --- ")
        (
            species,
            solid,
            si,
            species_sigma,
            solid_sigma,
            log_b,
            log_ks,
            ionic_strength,
        ) = self._compute()

        # Set the flag to signal a completed run
        self.done_flag = True

        # Create the table containing the species/comp. concentration
        self.species_distribution = pd.DataFrame(
            species,
            columns=self.species_names,
        ).rename_axis(columns="Species Conc. [mol/L]")
        self.species_distribution = self._setDataframeIndex(self.species_distribution)

        # Create the table containing the solid species "concentration"
        self.solid_distribution = pd.DataFrame(
            solid, columns=self.solid_names
        ).rename_axis(columns="Solid Conc. [mol/L]")
        check = self.solid_distribution.apply(
            lambda x: pd.Series(
                ["*" if i > 0 else "" for i in x],
                index=["Prec." + name for name in self.solid_distribution.columns],
                dtype=str,
            ),
            axis=1,
        )
        saturation_index = pd.DataFrame(
            si, columns=["SI" + name for name in self.solid_names]
        )

        self.solid_distribution = pd.merge(
            self.solid_distribution, check, left_index=True, right_index=True, sort=True
        )

        self.solid_distribution = pd.merge(
            self.solid_distribution,
            saturation_index,
            left_index=True,
            right_index=True,
            sort=True,
        )

        self.solid_distribution = self.solid_distribution[
            list(
                sum(
                    zip(
                        check.columns, saturation_index, self.solid_distribution.columns
                    ),
                    (),
                )
            )
        ]
        self.solid_distribution = self._setDataframeIndex(self.solid_distribution)

        # Compute and create table with percentages of species with respect to component
        # As defined with the input
        if self.distribution:
            cans = np.insert(self.c_tot, self.ind_comp, 0, axis=1)
        else:
            cans = self.c_tot

        species_perc_table = self._computePercTable(
            cans, species, self.model, self.species_perc_int
        )
        solid_perc_table = self._computePercTable(
            cans, solid, self.solid_model, self.solid_perc_int, solids=True
        )

        # Percentages are rounded two the second decimal and stored in a dataframe
        self.species_percentages = (
            pd.DataFrame(
                species_perc_table,
                columns=[self.species_names, self.species_perc_str],
            )
            .rename_axis(columns=["Species", r"% relative to comp."])
            .round(2)
        )
        self.species_percentages = self._setDataframeIndex(self.species_percentages)

        self.solid_percentages = (
            pd.DataFrame(
                solid_perc_table,
                columns=[self.solid_names, self.solid_perc_str],
            )
            .rename_axis(columns=["Solids", r"% relative to comp."])
            .round(2)
        )
        self.solid_percentages = self._setDataframeIndex(self.solid_percentages)

        # For error propagation create the corresponding tables
        self.species_sigma = pd.DataFrame(
            species_sigma, columns=self.species_names
        ).rename_axis(columns="Species Std. Dev. [mol/L]")
        self.species_sigma = self._setDataframeIndex(self.species_sigma)

        self.solid_sigma = pd.DataFrame(
            solid_sigma, columns=self.solid_names
        ).rename_axis(columns="Solid Std. Dev. [mol]")
        self.solid_sigma = self._setDataframeIndex(self.solid_sigma)

        # If working at variable ionic strength
        if self.imode == 1:
            # Add multi index to the species distribution containing the ionic strength
            self.species_distribution.insert(0, "I", ionic_strength)
            self.species_distribution.set_index("I", append=True, inplace=True)
            if self.nf > 0:
                self.solid_distribution.insert(0, "I", ionic_strength)
                self.solid_distribution.set_index("I", append=True, inplace=True)

            # Create table containing adjusted LogB for each point
            self.log_beta = pd.DataFrame(
                log_b[:, self.nc :],
                columns=self.species_names[self.nc :],
            ).rename_axis(columns="Formation Constants")
            self.log_beta = self._setDataframeIndex(self.log_beta)

            self.log_beta.insert(0, "I", ionic_strength)
            self.log_beta.set_index("I", append=True, inplace=True)

            # Create table containing adjusted LogKs for each point
            self.log_ks = pd.DataFrame(
                log_ks,
                columns=self.solid_names,
            ).rename_axis(columns="Solubility Products")
            self.log_ks = self._setDataframeIndex(self.log_ks)

            self.log_ks.insert(0, "I", ionic_strength)
            self.log_ks.set_index("I", append=True, inplace=True)

        logging.info("--- CALCULATION TERMINATED ---")

        return True

    def speciesDistribution(self):
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
        Returns the table containing formation constants and the ionic strength.
        """
        if self.done_flag == True:
            return self.log_beta
        else:
            return False

    def solubilityProducts(self):
        """
        Returns the table containing the LogKps for the solid species present in the model.
        """
        if self.done_flag == True:
            return self.log_ks
        else:
            return False

    def percentages(self):
        """
        Return percentages of species with respect to the desired component.
        """
        if self.done_flag == True:
            return self.species_percentages, self.solid_percentages
        else:
            return False

    def sigmas(self):
        """
        Return percentages of species with respect to the desired component.
        """
        if self.done_flag == True:
            return self.species_sigma, self.solid_sigma
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

            if self.nf > 0:
                solid_info = pd.DataFrame(
                    {
                        "logKs": self.log_ks_ris,
                    },
                    index=self.solid_names,
                ).rename_axis(index="Solid Names")
            else:
                solid_info = None

            if self.imode == 1:
                species_info.insert(1, "Ref. I", self.species_ris[self.nc :])
                species_info.insert(2, "Charge", self.species_charges[self.nc :])
                species_info.insert(3, "C", self.species_cg[self.nc :])
                species_info.insert(4, "D", self.species_dg[self.nc :])
                species_info.insert(5, "E", self.species_eg[self.nc :])

                if self.nf > 0:
                    solid_info.insert(1, "Ref. I", self.solid_ris)
                    solid_info.insert(2, "Charge", self.solid_charges)
                    solid_info.insert(3, "C", self.solid_cg)
                    solid_info.insert(4, "D", self.solid_dg)
                    solid_info.insert(5, "E", self.solid_eg)

            if self.errors:
                species_info.insert(1, "Sigma logB", self.log_beta_sigma)

                if self.nf > 0:
                    solid_info.insert(1, "Sigma logKs", self.log_ks_sigma)

            comp_info = pd.DataFrame(
                {
                    "Charge": self.comp_charge,
                },
                index=self.species_names[: self.nc],
            ).rename_axis(index="Components Names")

            if self.distribution:
                comp_info["Tot. C."] = np.insert(self.c_tot[0], self.ind_comp, None)
                if self.errors:
                    comp_info.insert(2, "Sigma Tot C", self.c0_sigma)
            else:
                comp_info["Vessel Conc."] = self.initial_c
                comp_info["Titrant Conc."] = self.c_added
                if self.errors:
                    comp_info.insert(2, "Sigma C0", self.c0_sigma)
                    comp_info.insert(4, "Sigma cT", self.ct_sigma)

            return species_info, solid_info, comp_info
        else:
            return False

    def _compute(self):
        """
        Calculate species distribution.
        """
        # Initialize array to contain the species concentration
        # obtained from the calculations
        for_estimation_c = []
        results_species_conc = []
        results_solid_conc = []
        results_solid_si = []
        results_species_sigma = []
        results_solid_sigma = []
        results_log_b = []
        results_log_ks = []
        results_ionic_strength = []

        # Cycle over each point of titration
        for point in range(self.nop):
            logging.debug("--> OPTIMIZATION POINT: {}".format(point))

            if self.distribution:
                c, fixed_c = self._distributionGuess(point, for_estimation_c)
            else:
                fixed_c = None
                c = self._titrationGuess(point, for_estimation_c)

            # Initial guess for solids conentrations should always be zero
            cp = np.zeros(self.nf)

            logging.debug("INITIAL ESTIMATED FREE C: {}".format(c))
            logging.debug("TOTAL C: {}".format(self.c_tot[point]))

            # Calculate species concnetration or each curve point
            (
                species_conc_calc,
                solid_conc_calc,
                log_b,
                log_ks,
                ionic_strength,
            ) = self._newtonRaphson(
                point,
                c,
                cp,
                self.c_tot[point],
                fixed_c,
            )

            # Store concentrations before solid precipitation to estimate next points c
            for_estimation_c.append(species_conc_calc)

            saturation_index_calc = np.zeros(self.nf)

            for _ in range(self.nf):
                saturation_index = self._getSaturationIndex(
                    species_conc_calc[: self.nc], log_ks
                )
                if any(i > 1.000000001 for i in saturation_index):
                    (
                        species_conc_calc,
                        solid_conc_calc,
                        log_b,
                        log_ks,
                        ionic_strength,
                    ) = self._newtonRaphson(
                        point,
                        species_conc_calc[: self.nc],
                        solid_conc_calc,
                        self.c_tot[point],
                        fixed_c,
                        with_solids=True,
                    )

                    saturation_index_calc[
                        np.argmax(saturation_index)
                    ] = saturation_index = self._getSaturationIndex(
                        species_conc_calc[: self.nc], log_ks
                    )[
                        np.argmax(saturation_index)
                    ]
                else:
                    saturation_index_calc = np.maximum(
                        saturation_index_calc, saturation_index
                    )
                    break

            if self.errors:
                species_sigma, solid_sigma = self._computeErrors(
                    species_conc_calc, log_b, point
                )
            else:
                species_sigma = np.array([None for i in range(self.nc + self.ns)])
                solid_sigma = np.array([None for i in range(self.nf)])

            # Store calculated species/solid concentration into a vector
            results_species_conc.append(species_conc_calc)
            results_solid_conc.append(solid_conc_calc)

            results_solid_si.append(saturation_index_calc)
            # Store uncertainty for calculated values
            results_species_sigma.append(species_sigma)
            results_solid_sigma.append(solid_sigma)
            # Store calculated ionic strength
            results_ionic_strength.append(ionic_strength)
            # Store calculated LogB/LogKs
            results_log_b.append(log_b)
            results_log_ks.append(log_ks)

        # Stack calculated species concentration/logB/ionic strength in tabular fashion
        results_species_conc = np.stack(results_species_conc)
        results_solid_conc = np.stack(results_solid_conc)
        results_solid_si = np.stack(results_solid_si)
        results_species_sigma = np.stack(results_species_sigma)
        results_solid_sigma = np.stack(results_solid_sigma)
        results_log_b = np.stack(results_log_b)
        results_log_ks = np.stack(results_log_ks)
        results_ionic_strength = np.stack(results_ionic_strength)

        # Return distribution/logb/ionic strength
        return (
            results_species_conc,
            results_solid_conc,
            results_solid_si,
            results_species_sigma,
            results_solid_sigma,
            results_log_b,
            results_log_ks,
            results_ionic_strength,
        )

    def _newtonRaphson(self, point, c, cp, c_tot, fixed_c, with_solids=False):
        # FIXME: FOR DEBUGGING PURPOSES
        # np.seterr("print")
        iteration = 0

        if not with_solids:
            # If working with variable ionic strength ompute initial guess for species concentration
            if self.imode == 1:
                if point == 0:
                    log_beta, log_ks, _ = self._updateConstants(
                        c_tot,
                        self.log_beta_ris,
                        self.log_ks_ris,
                        self.comp_charge,
                        point,
                        first_guess=True,
                    )
                else:
                    log_beta = self.previous_log_beta
                    log_ks = self.previous_log_ks

                logging.debug(
                    "Estimate of LogB for point {}: {}".format(point, log_beta)
                )

                c, c_spec = self._damping(point, c, cp, log_beta, c_tot, fixed_c)

                log_beta, log_ks, cis = self._updateConstants(
                    c_spec,
                    self.log_beta_ris,
                    self.log_ks_ris,
                    self.species_charges,
                    point,
                )

                self.previous_log_beta = log_beta
                self.previous_log_ks = log_ks
                logging.debug("Updated LogB: {}".format(log_beta))
            else:
                log_beta = self.log_beta_ris
                log_ks = self.log_ks_ris
                c, c_spec = self._damping(point, c, cp, log_beta, c_tot, fixed_c)
                cis = [None]
        else:
            if self.imode == 1:
                c_tot_calc, c_spec = self._speciesConcentration(
                    c, cp, self.previous_log_beta
                )
                log_beta, log_ks, cis = self._updateConstants(
                    c_spec,
                    self.log_beta_ris,
                    self.log_ks_ris,
                    self.species_charges,
                    point,
                )

                self.previous_log_beta = log_beta
                self.previous_log_ks = log_ks
            else:
                log_beta = self.log_beta_ris
                log_ks = self.log_ks_ris
                cis = [None]

        # Calculate total concentration given the species concentration
        c_tot_calc, c_spec = self._speciesConcentration(c, cp, log_beta)

        # Calculate saturation index for solid species if any
        saturation_index = self._getSaturationIndex(c, log_ks)

        # Check which solids are to be considered
        shifts_to_calculate, shifts_to_skip = self._checkSolidsSaturation(
            saturation_index
        )

        # Compute difference between total concentrations and calculated one
        delta, can_delta, solid_delta = self._computeDelta(
            c_tot,
            c_tot_calc,
            with_solids,
            saturation_index,
            shifts_to_calculate[-self.nf :],
        )

        while iteration < 200:
            logging.debug(
                "-> BEGINNING NEWTON-RAPHSON ITERATION {} ON POINT {}".format(
                    iteration, point
                )
            )

            # Compute Jacobian
            J = self._computeJacobian(
                c_spec,
                saturation_index,
                with_solids,
                shifts_to_skip[-self.nf :],
            )

            # J, delta = self._scaleMatrix(J, delta, with_solids)

            if self.distribution:
                # Ignore row and column relative to the indipendent component
                J = np.delete(J, self.ind_comp, axis=0)
                J = np.delete(J, self.ind_comp, axis=1)

            # Solve the equations to obtain newton step
            shifts = np.linalg.solve(J, -delta)

            if with_solids:
                actual_shifts = np.zeros(len(shifts_to_calculate))
                actual_shifts[shifts_to_calculate] = shifts
                shifts = actual_shifts

            if self.distribution:
                shifts = np.insert(shifts, self.ind_comp, 0, axis=0)
            logging.debug(
                "Shifts to be applied to concentrations and precipitates: {}".format(
                    shifts
                )
            )

            if with_solids:
                one_over_del = -shifts / (0.5 * np.append(c, cp))
            else:
                one_over_del = -shifts / (0.5 * c)

            one_over_del = np.where(one_over_del > 1, one_over_del, 1)
            rev_del = 1 / one_over_del

            c = c + rev_del[: self.nc] * shifts[: self.nc]

            if with_solids:
                cp = cp + rev_del[self.nc :] * shifts[self.nc :]

            logging.debug("Newton-Raphson updated free concentrations: {}".format(c))
            logging.debug(
                "Newton-Raphson updated precipitate concentrations: {}".format(cp)
            )

            # Calculate total concentration given the updated free/precipitate concentration
            c_tot_calc, c_spec = self._speciesConcentration(c, cp, log_beta)

            # Compute difference between total concentrations and convergence
            saturation_index = self._getSaturationIndex(c, log_ks)

            # Compute difference between total concentrations
            delta, can_delta, solid_delta = self._computeDelta(
                c_tot,
                c_tot_calc,
                with_solids,
                saturation_index,
                shifts_to_calculate[-self.nf :],
            )

            comp_conv_criteria = np.sum(
                (can_delta[c_tot != 0] / c_tot[c_tot != 0]) ** 2
            )

            logging.debug(
                "Convergence for analytical concentrations at Point {} iteration {}: {}".format(
                    point, iteration, comp_conv_criteria
                )
            )
            iteration += 1
            # If convergence criteria is met return check if any solid has to be considered
            if comp_conv_criteria < 1e-16:
                if with_solids:
                    if all(abs(i) <= 1e-9 for i in solid_delta):
                        return c_spec, cp, log_beta, log_ks, cis
                else:
                    return c_spec, cp, log_beta, log_ks, cis

        # If during the first or second run you exceed the iteration limit report it
        logging.error(
            "Calculation terminated early, no convergence found at point {} in {} iterations".format(
                point, iteration
            )
            + (
                (
                    " after solids were considered."
                    if with_solids
                    else " before solids were considered."
                )
                if self.nf > 0
                else ""
            )
        )
        raise Exception(
            "Calculation of species concentration aborted, no convergence found with conc {} at point {} in {} iterations".format(
                str(c_spec), point, iteration
            )
            + (
                (
                    " after solids were considered."
                    if with_solids
                    else " before solids were considered."
                )
                if self.nf > 0
                else ""
            )
        )

    def _checkSolidsSaturation(self, saturation_index):
        # Solid species to consider have saturation index over 1
        # cp_to_calculate = saturation_index > 1
        if saturation_index.size != 0:
            cp_to_calculate = np.where(
                (saturation_index == np.max(saturation_index)) & (saturation_index > 1),
                True,
                False,
            )
            shifts_to_calculate = np.concatenate(
                ([True for i in range(self.nc)], cp_to_calculate)
            )
        else:
            shifts_to_calculate = np.array([True for i in range(self.nc)])

        shifts_to_skip = ~shifts_to_calculate

        if self.distribution:
            # If calculating distribution of species exclude the indipendent component from the species to consider
            shifts_to_calculate = np.delete(shifts_to_calculate, self.ind_comp, axis=0)
            shifts_to_skip = np.delete(shifts_to_skip, self.ind_comp, axis=0)
        return shifts_to_calculate, shifts_to_skip

    def _computeDelta(
        self, c_tot, c_tot_calc, with_solids, saturation_index, cp_to_calculate
    ):
        can_delta = c_tot_calc - c_tot

        if with_solids:
            solid_delta = np.ones(self.nf) - saturation_index
            solid_delta = solid_delta[cp_to_calculate]
        else:
            solid_delta = []

        delta = np.concatenate((can_delta, solid_delta))
        # delta = can_delta
        return delta, can_delta, solid_delta

    def _computeJacobian(self, c_spec, saturation_index, with_solids, to_skip):
        if with_solids:
            nt = self.nc + self.nf
            to_skip = np.concatenate(
                (np.array([False for i in range(self.nc)]), to_skip)
            )
        else:
            nt = self.nc

        J = np.zeros(shape=(nt, nt))

        # Compute Jacobian
        # Jacobian for acqueous species
        for j in range(self.nc):
            for k in range(self.nc):
                J[j, k] = np.sum(self.model[j] * self.model[k] * (c_spec / c_spec[k]))

        if with_solids:
            # Jacobian for solid species
            for j in range(self.nc):
                for k in range(self.nc, nt):
                    J[j, k] = self.solid_model[j, (k - self.nc)]

            for j in range(self.nc, nt):
                for k in range(self.nc):
                    J[j, k] = np.negative(self.solid_model[k, (j - self.nc)]) * (
                        saturation_index[(j - self.nc)] / c_spec[k]
                    )

            for j in range(self.nc, nt):
                for k in range(self.nc, nt):
                    J[j, k] = 0

            # Remove rows and columns referring to under-saturated solids
            J = np.delete(J, to_skip, axis=0)
            J = np.delete(J, to_skip, axis=1)

        return J

    # def _scaleMatrix(self, J, delta, with_solids):
    #     if with_solids:
    #         nt = self.nc + self.nf
    #         to_skip = np.concatenate(
    #             (np.array([False for i in range(self.nc)]), to_skip)
    #         )
    #     else:
    #         nt = self.nc

    #     print(nt)

    #     for j in range(nt):
    #         for k in range(nt):
    #             J[j, k] = J[j, k] * ((J[k, k] * J[j, j]) ** -0.5)

    #     print(J)

    #     print(delta)

    #     for k in range(nt - (1 if self.distribution else 0)):
    #         delta[k] = delta[k] * ((J[k, k]) ** -0.5)

    #     print(delta)

    #     return J, delta

    # TODO: document functions
    def _speciesConcentration(self, c, cp, log_beta):
        """
        Calculate species concentration it returns c_spec and c_tot_calc:
        - c_spec[0->nc] = free conc for each component.
        - c_spec[nc+1->nc+ns] = species concentrations.
        - c_tot_calc = estimated anaytical concentration.
        """
        log_c = np.log10(c)
        tiled_log_c = np.tile(log_c, [self.ns + self.nc, 1]).T
        log_spec_mat = tiled_log_c * self.model
        log_c_spec = np.sum(log_spec_mat, axis=0) + log_beta
        log_c_spec = self._checkOverUnderFlow(log_c_spec)
        c_spec = 10**log_c_spec
        logging.debug("Species Concentrations: %s", c_spec)

        tiled_cp = np.tile(cp, [self.nc, 1])

        # Estimate total concentration given the species concentration
        c_tot_calc = np.sum(self.model * np.tile(c_spec, [self.nc, 1]), axis=1) + (
            np.sum(self.solid_model * tiled_cp, axis=1) if self.nf > 0 else 0
        )

        if self.distribution:
            # Take out the analytical concentration relative to the indipendent component
            c_tot_calc = np.delete(c_tot_calc, self.ind_comp, 0)

        logging.debug("Calculated Total Concentration: %s", c_tot_calc)

        return c_tot_calc, c_spec

    def _distributionGuess(self, point, for_estimation_c):
        """
        Return an initial guess for the first newton raphson iteration when dealing with distributions of species
        """
        fixed_c = self.ind_comp_c[point]
        # Initial guess of free concentration (c) is considered as follows:
        #   - First point as a fraction of the total concentration
        #   - Second and third points as estimate from previous point
        #   - Subsequent points are extrapolated as follows
        if point > 2:
            lp1 = -np.log10(for_estimation_c[(point - 1)][: self.nc])
            lp2 = -np.log10(for_estimation_c[(point - 2)][: self.nc])
            lp3 = -np.log10(for_estimation_c[(point - 3)][: self.nc])

            # If two subsequent points present the same concentration
            # avoid the issue by using simply the previous point concentration
            c = np.where(lp2 == lp3, lp1, (lp1 + ((lp1 - lp2) ** 2) / (lp2 - lp3)))
            # If the extrapolation returns valuse that would cause under/overflow adjust them accordingly
            c = self._checkOverUnderFlow(c, d=2)

            if (c < 0).any():
                c = lp1

            # Convert logs back to concentrations
            c = 10 ** (-c)
            # Free C of indipendent component is set as defined in the settings tab
            c[self.ind_comp] = fixed_c
            logging.debug("ESTIMATED C WITH INTERPOLATION")
        elif point > 0:
            c = for_estimation_c[(point - 1)][: self.nc].copy()
            c[self.ind_comp] = fixed_c
            logging.debug("ESTIMATED C FROM PREVIOUS POINT")
        elif point == 0:
            c = np.multiply(self.c_tot[0], 0.001)
            c = np.insert(c, self.ind_comp, fixed_c)
            logging.debug("ESTIMATED C AS FRACTION TOTAL C")
        return c, fixed_c

    def _titrationGuess(self, point, for_estimation_c):
        """
        Return an initial guess for the first newton raphson iteration when dealing with simulated titrations
        """
        # Initial guess of free concentration (c) is considered as follows:
        #   - First point as a fraction of the total concentration
        #   - Second and third points as estimate from previous point
        #   - Subsequent points are extrapolated as follows
        if point > 2:
            v = self.v_added[point]
            v1 = self.v_added[(point - 1)]
            v2 = self.v_added[(point - 2)]
            v3 = self.v_added[(point - 3)]
            lp1 = -np.log10(for_estimation_c[(point - 1)][: self.nc])
            lp2 = -np.log10(for_estimation_c[(point - 2)][: self.nc])
            lp3 = -np.log10(for_estimation_c[(point - 3)][: self.nc])

            # If two subsequent points present the same concentration
            # avoid the issue by using simply the previous point concentration
            c = np.where(
                lp2 == lp3,
                lp1,
                (
                    lp1
                    + (((lp1 - lp2) / (v1 - v2)) ** 2)
                    * ((v2 - v3) / (lp2 - lp3))
                    * (v - v1)
                ),
            )
            # If the extrapolation returns valuse that would cause under/overflow adjust them accordingly
            c = self._checkOverUnderFlow(c, d=2)

            if (c < 0).any():
                c = lp1

            # Convert logs back to concentrations
            c = 10 ** (-c)
            logging.debug("ESTIMATED C WITH INTERPOLATION")
        elif point > 0:
            c = for_estimation_c[(point - 1)][: self.nc]
            logging.debug("ESTIMATED C FROM PREVIOUS POINT")
        elif point == 0:
            c = np.multiply(self.c_tot[0], 0.001)
            logging.debug("ESTIMATED C AS FRACTION TOTAL C")

        return c

    def _checkOverUnderFlow(self, c, d=1):
        """
        Given c check if any of the given log of concentrations would give overflow or underflow errors, adjust accordingly
        """
        c = np.where(c > (self.epsl / d), (self.epsl / d), c)
        c = np.where(c < (-self.epsl / d), (-self.epsl / d), c)
        return c

    def _setBHParams(self, species, to_remove, past, zast, c, d, e, solids=False):
        # Retrive CG/DG/EG for each of the species
        # Remove values that refers to ignored comps
        cg = species.iloc[:, 5].to_numpy(dtype="float")
        dg = species.iloc[:, 6].to_numpy(dtype="float")
        eg = species.iloc[:, 7].to_numpy(dtype="float")
        cg = np.delete(cg, to_remove, axis=0)
        dg = np.delete(dg, to_remove, axis=0)
        eg = np.delete(eg, to_remove, axis=0)

        if not solids:
            # If computing solution species adds values for components
            cg = np.insert(cg, 0, [0 for i in range(self.nc)])
            dg = np.insert(dg, 0, [0 for i in range(self.nc)])
            eg = np.insert(eg, 0, [0 for i in range(self.nc)])

        use_reference = (cg == 0) + (dg == 0) + (eg == 0)

        # Compute CG/DG/EG terms of D-H
        reference_cg = c[0] * past + c[1] * zast
        reference_dg = d[0] * past + d[1] * zast
        reference_eg = e[0] * past + e[1] * zast

        cg = np.where(use_reference, reference_cg, cg)
        dg = np.where(use_reference, reference_dg, dg)
        eg = np.where(use_reference, reference_eg, eg)

        return cg, dg, eg

    def _damping(self, point, c, cp, log_beta, c_tot, fixed_c):
        logging.debug("ENTERING DAMP ROUTINE")

        epsilon = 2.5e-1 if point > 0 else 1e-9
        model = self.model
        nc = self.nc
        if self.distribution:
            nc -= 1
            model = np.delete(model, self.ind_comp, axis=0)
            model = np.delete(model, self.ind_comp, axis=1)

        coeff = np.array([0 for i in range(nc)])
        a0 = np.max(model, axis=1)

        iteration = 0
        while iteration < 1000:
            _, c_spec = self._speciesConcentration(c, cp, log_beta)

            if self.distribution:
                c_spec = np.delete(c_spec, self.ind_comp)

            c_times_model = np.tile(c_spec, [nc, 1]) * model

            sum_reac = np.where(model > 0, c_times_model, 0).sum(axis=1) + np.where(
                c_tot < 0, np.abs(c_tot), 0
            )
            sum_prod = np.where(c_tot >= 0, c_tot, 0) - np.where(
                model < 0, c_times_model, 0
            ).sum(axis=1)

            conv_criteria = (sum_reac - sum_prod) / (sum_reac + sum_prod)
            # print(conv_criteria)

            if all(i < epsilon for i in conv_criteria):
                logging.debug(
                    f"CONVERGENCE! EXITING DAMP ROUTINE AFTER {iteration} ITERATIONS"
                )
                if self.distribution:
                    c_spec = np.insert(c_spec, self.ind_comp, fixed_c)
                return c, c_spec

            new_coeff = (
                0.1
                - np.where(
                    (sum_reac > sum_prod), (sum_prod / sum_reac), (sum_reac / sum_prod)
                )
                * 0.08
            )

            if iteration == 0:
                coeff = new_coeff
            coeff = np.where(new_coeff > coeff, new_coeff, coeff)

            if self.distribution:
                c = np.delete(c, self.ind_comp)
            c = coeff * c * (sum_prod / sum_reac) ** (1 / a0) + (1 - coeff) * c
            if self.distribution:
                c = np.insert(c, self.ind_comp, fixed_c)

            iteration += 1

        logging.debug(
            f"WARNING! EXITING DAMP ROUTINE AFTER {iteration} ITERATIONS WITHOUT CONVERGENCE"
        )
        if self.distribution:
            c_spec = np.insert(c_spec, self.ind_comp, fixed_c)
        return c, c_spec

        # if self.distribution:
        #     c_spec = np.insert(c_spec, self.ind_comp, fixed_c)
        # return c, c_spec
        # raise Exception(
        #     "Dampening routine couldn't find a solution at point {}".format(point)
        # )

    def _getSaturationIndex(self, c, log_ks):
        if self.nf > 0:
            tiled_c = np.tile(c, [self.nf, 1]).T
            saturation_index = np.prod(tiled_c**self.solid_model, axis=0) / (
                10**log_ks
            )
            return saturation_index
        else:
            return np.array([])

    def _ionicStr(self, c, charges, point, first_guess):
        """
        Calculate ionic strength given concentrations of species and their charges.
        """
        if first_guess:
            I = ((c * (charges**2)).sum() / 2) + self.background_c[point]
        else:
            I = ((c * (charges**2)).sum() + self.background_c[point]) / 2

        return I

    def _updateConstants(self, c, log_beta, log_ks, charges, point, first_guess=False):
        if first_guess and self.distribution:
            c = np.insert(c, self.ind_comp, 0, axis=0)

        cis = self._ionicStr(c, charges, point, first_guess)
        logging.debug(
            "Current I: {}".format(cis) + ("\tFIRST GUESS" if first_guess else "")
        )
        updated_log_b = self._updateLogB(cis, log_beta)
        updated_log_ks = self._updateLogKs(cis, log_ks)
        return updated_log_b, updated_log_ks, cis

    def _updateLogKs(self, cis, log_ks):
        cis = np.tile(cis, self.nf)
        radqcis = np.sqrt(cis)
        fib2 = radqcis / (1 + (self.b * radqcis))
        updated_log_ks = (
            log_ks
            + self.solid_az * (fib2 - self.solid_fib)
            - self.solid_cg * (cis - self.solid_ris)
            - self.solid_dg * ((cis * radqcis) - (self.solid_ris * self.solid_radqris))
            - self.solid_eg * ((cis**2) - (self.solid_ris**2))
        )

        return updated_log_ks

    def _updateLogB(self, cis, log_beta):
        """
        Update formation constants of species given the current
        """
        cis = np.tile(cis, self.nc + self.ns)
        radqcis = np.sqrt(cis)
        fib2 = radqcis / (1 + (self.b * radqcis))
        updated_log_beta = (
            log_beta
            - self.species_az * (fib2 - self.species_fib)
            + self.species_cg * (cis - self.species_ris)
            + self.species_dg
            * ((cis * radqcis) - (self.species_ris * self.species_radqris))
            + self.species_eg * ((cis**2) - (self.species_ris**2))
        )

        return updated_log_beta

    def _computePercTable(self, cans, calculated_c, model, percent_to, solids=False):
        can_to_perc = np.array(
            [
                [cans[point, index] for index in percent_to]
                for point in range(cans.shape[0])
            ]
        )

        if not solids:
            can_to_perc = np.concatenate((cans, can_to_perc), axis=1)
        adjust_factor = np.array(
            [
                model[component, index + (self.nc if not solids else 0)]
                for index, component in enumerate(percent_to)
            ]
        )
        adjust_factor = np.where(adjust_factor <= 0, 1, adjust_factor)
        if not solids:
            adjust_factor = np.concatenate(
                ([1 for component in range(self.nc)], adjust_factor), axis=0
            )

        perc_table = np.where(
            can_to_perc == 0, 0, (calculated_c * adjust_factor) / can_to_perc
        )
        perc_table = perc_table * 100

        return perc_table

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

        return species_perc_int.astype(int), solid_perc_int.astype(int)

    def _computeErrors(self, c_spec, log_b, point):

        # Get betas from log betas
        beta = 10 ** log_b[self.nc :]
        model = self.model[:, self.nc :]
        free_c = c_spec[: self.nc]
        c_spec = c_spec[self.nc :]
        # Define dimension of arrays required
        M = np.zeros(shape=(self.nc, self.nc))
        der_free_beta = np.zeros(shape=(self.nc, self.ns))
        der_free_tot = np.zeros(shape=(self.nc, self.nc))
        der_spec_beta = np.zeros(shape=(self.ns, self.ns))
        der_spec_tot = np.zeros(shape=(self.ns, self.nc))
        b = np.zeros(shape=(self.nc, self.ns))
        d = np.zeros(shape=(self.nc, self.nc))

        # Compute common matrix term
        for j in range(self.nc):
            for k in range(self.nc):
                M[j, k] = np.sum(model[j] * model[k] * (c_spec / free_c[k])) + (
                    1 if j == k else 0
                )

        for i in range(self.ns):
            for j in range(self.nc):
                b[j, i] = -model[j, i] * (c_spec[i] / beta[i])

        for r in range(self.nc):
            for j in range(self.nc):
                d[j, r] = 1 if j == r else 0

        for i in range(self.ns):
            der_free_beta[:, i] = np.linalg.solve(M, b[:, i])

        for r in range(self.nc):
            der_free_tot[:, r] = np.linalg.solve(M, d[:, r])

        if self.distribution:
            der_free_beta[self.ind_comp, :] = 0
            der_free_tot[self.ind_comp, :] = 0

        for i in range(self.ns):
            for l in range(self.ns):
                der_spec_beta[i, l] = (1 if i == l else 0) * (
                    c_spec[i] / beta[l]
                ) + np.sum(model[:, i] * (c_spec[i] / free_c) * der_free_beta[:, l])

        for i in range(self.ns):
            for r in range(self.nc):
                der_spec_tot[i, r] = np.sum(
                    model[:, i] * (c_spec[i] / free_c) * der_free_tot[:, r]
                )

        comp_sigma = np.sqrt(
            ((der_free_beta**2) * (self.beta_sigma**2)).sum(axis=1)
            + ((der_free_tot**2) * (self.conc_sigma[point] ** 2)).sum(axis=1)
        )

        species_sigma = np.sqrt(
            ((der_spec_beta**2) * (self.beta_sigma**2)).sum(axis=1)
            + ((der_spec_tot**2) * (self.conc_sigma[point] ** 2)).sum(axis=1)
        )
        species_sigma = np.concatenate((comp_sigma, species_sigma))

        # FIXME: we need to implement propagation error for solid concentrations
        solid_sigma = np.array([None for i in range(self.nf)])

        return species_sigma, solid_sigma

    def _speciesNames(self, model):
        """
        Returns species names as brute formula from comp names and coefficients
        """
        model = model.T
        names = []

        # TODO: vectorize the operation
        for i in range(len(model)):
            names.append("")
            for j, comp in enumerate(self.comp_names):
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

    def _setDataframeIndex(self, dataframe):
        if self.distribution:
            dataframe = dataframe.set_index(self.ind_comp_logs).rename_axis(
                index="p[" + self.comp_names[self.ind_comp] + "]",
            )
        else:
            dataframe = dataframe.set_index(self.v_added).rename_axis(
                index="Added Volume [l]",
            )

        return dataframe
