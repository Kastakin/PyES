import numpy as np
import pytest
from numpy.testing import assert_equal
from utils import compare_results, get_input, get_results

from src.main.python.pyes.optimizers.distribution import Distribution


class TestDistribution:
    optimizer = Distribution()

    def test_create_optimizer(self):
        assert type(self.optimizer) is Distribution
        assert self.optimizer.done_flag is False
        assert type(self.optimizer.epsl) is int

    def test_fit_optimizer(self):
        self.optimizer.fit(get_input("acetico_solido_fake", opt_type="distribution"))
        # Test that after fitting the model is stil unsolved
        assert self.optimizer.done_flag is False

        # Test that we are working in distribution mode
        assert self.optimizer.distribution is True

        # Test error and ionic strength mode
        assert self.optimizer.errors is True
        assert self.optimizer.imode == 1

        # Test correct number of species/components present
        assert self.optimizer.nc == 2
        assert self.optimizer.ns == 2
        assert self.optimizer.nf == 2

        # Test corrected index of independent component
        assert self.optimizer.ind_comp == 1

        # Test components charges
        assert_equal(self.optimizer.comp_charge, np.array([-1, 1]))

        # Test models
        assert_equal(self.optimizer.model, np.array([[1, 0, 0, 1], [0, 1, -1, 1]]))
        assert_equal(self.optimizer.solid_model, np.array([[1, 1], [1, -1]]))

        # Test names
        assert_equal(self.optimizer.comp_names, np.array(["A", "H"]))
        assert_equal(
            self.optimizer.species_names, np.array(["A", "H", "(OH)", "(A)(H)"])
        )
        assert_equal(self.optimizer.solid_names, np.array(["(A)(H)", "(A)(OH)"]))

    @pytest.mark.parametrize(
        "input_data, true_result",
        zip(
            get_input(opt_type="distribution").values(),
            get_results("pyes", opt_type="distribution").values(),
        ),
        ids=get_input(opt_type="distribution").keys(),
    )
    def test_pyes_results(self, input_data, true_result):
        compare_results(Distribution(), input_data, true_result)

    @pytest.mark.parametrize(
        "input_data, true_result",
        zip(
            get_input(opt_type="distribution").values(),
            get_results("es4", opt_type="distribution").values(),
        ),
        ids=get_input(opt_type="distribution").keys(),
    )
    def test_es4_results(self, input_data, true_result):
        compare_results(Distribution(), input_data, true_result)

    @pytest.mark.parametrize(
        "input_data, true_result",
        zip(
            get_input(opt_type="distribution").values(),
            get_results("hyss", opt_type="distribution").values(),
        ),
        ids=get_input(opt_type="distribution").keys(),
    )
    def test_hyss_results(self, input_data, true_result):
        compare_results(Distribution(), input_data, true_result)
