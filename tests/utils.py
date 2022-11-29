import json
from pathlib import Path
from typing import Any, Dict, Union

import numpy as np
import pandas as pd
import pytest
from numpy.testing import assert_allclose

RTOL = 5e-2


def compare_results(opt, input_data, true_result):
    if true_result is None:
        pytest.skip("No data found for given source")

    opt.fit(input_data)
    opt.predict()

    # Test that optimizer exited gracefully
    assert opt.done_flag is True

    result = {
        "logb": opt.formationConstants(),
        "logks": opt.solubilityProducts(),
        "solid_distribution": opt.solidDistribution(),
        "solid_SD": opt.solidSigmas(),
        "species_distribution": opt.speciesDistribution(),
        "species_SD": opt.speciesSigmas(),
    }

    for key, value in result.items():
        if not value.empty:
            result[key] = value.reset_index()

    # Test results for species
    assert_allclose(
        result["logb"].to_numpy(),
        true_result["logb"].to_numpy(),
        rtol=RTOL,
    )

    assert_allclose(
        result["species_distribution"].to_numpy(),
        true_result["species_distribution"].to_numpy(),
        rtol=RTOL,
        verbose=True,
    )

    assert_allclose(
        result["species_SD"].to_numpy(),
        true_result["species_SD"].to_numpy(),
        rtol=RTOL,
    )

    # Test results for solids
    assert_allclose(
        result["logks"].to_numpy(),
        true_result["logks"].to_numpy(),
        rtol=RTOL,
    )

    assert_allclose(
        result["solid_distribution"].replace("", np.nan).dropna(axis=1).to_numpy(),
        true_result["solid_distribution"].to_numpy(),
        rtol=RTOL,
    )

    assert_allclose(
        result["solid_SD"].to_numpy(),
        true_result["solid_SD"].to_numpy(),
        rtol=RTOL,
    )


def get_input(
    name: Union[str, None] = None, *, opt_type: str
) -> Union[Dict[str, Dict[str, Any]], Dict[str, Any]]:
    base_folder = Path().joinpath("tests", "test_data")
    data_folder = base_folder.joinpath(f"{opt_type}_data")
    subfolders = (folder for folder in data_folder.iterdir() if folder.is_dir())

    if name:
        with data_folder.joinpath(name, f"{name}.json").open() as f:
            return json.load(f)
    else:
        inputs = {}
        for folder in subfolders:
            input_name = folder.name
            with folder.joinpath(f"{input_name}.json").open() as f:
                inputs[input_name] = json.load(f)
        return inputs


def get_results(
    source: str, opt_type: str
) -> Dict[str, Union[None, Dict[str, pd.DataFrame]]]:
    base_folder = Path().joinpath("tests", "test_data")
    data_folder = base_folder.joinpath(f"{opt_type}_data")
    subfolders = (folder for folder in data_folder.iterdir() if folder.is_dir())

    results = {}
    for folder in subfolders:
        input_name = folder.name

        # If no folder for source is present or it's empty no data to collect
        if not folder.joinpath(source).is_dir():
            results[input_name] = None
            continue
        elif not any(folder.joinpath(source).iterdir()):
            results[input_name] = None
            continue

        result = {
            "logb": None,
            "logks": None,
            "solid_distribution": None,
            "solid_SD": None,
            "species_distribution": None,
            "species_SD": None,
        }

        for key in result.keys():
            try:
                result[key] = pd.read_csv(
                    folder.joinpath(source, f"{input_name}_{key}.csv"),
                    header=None,
                )
            except FileNotFoundError:
                result[key] = pd.DataFrame()

        results[input_name] = result

    return results
