import pytest
from utils import compare_results, get_input, get_results

from src.main.python.pyes.optimizers.distribution import Distribution


class TestTitration:
    optimizer = Distribution()

    @pytest.mark.parametrize(
        "input_data, true_result",
        zip(
            get_input(opt_type="titration").values(),
            get_results("pyes", opt_type="titration").values(),
        ),
        ids=get_input(opt_type="titration").keys(),
    )
    def test_pyes_results(self, input_data, true_result):
        compare_results(Distribution(), input_data, true_result)

    @pytest.mark.parametrize(
        "input_data, true_result",
        zip(
            get_input(opt_type="titration").values(),
            get_results("es4", opt_type="titration").values(),
        ),
        ids=get_input(opt_type="titration").keys(),
    )
    def test_es4_results(self, input_data, true_result):
        compare_results(Distribution(), input_data, true_result)

    @pytest.mark.parametrize(
        "input_data, true_result",
        zip(
            get_input(opt_type="titration").values(),
            get_results("hyss", opt_type="titration").values(),
        ),
        ids=get_input(opt_type="titration").keys(),
    )
    def test_hyss_results(self, input_data, true_result):
        compare_results(Distribution(), input_data, true_result)
