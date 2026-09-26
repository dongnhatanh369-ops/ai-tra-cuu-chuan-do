import pytest

from backend.app.calculator import CalculationError, average, calculate_analyte_concentration


def test_hcl_naoh_one_to_one():
    result = calculate_analyte_concentration(
        analyte_volume=25,
        analyte_volume_unit="mL",
        titrant_volume=23.6,
        titrant_volume_unit="mL",
        titrant_molarity=0.1,
    )
    assert result.analyte_molarity == pytest.approx(0.0944)


def test_reaction_coefficients_are_applied():
    result = calculate_analyte_concentration(
        analyte_volume=10,
        analyte_volume_unit="mL",
        titrant_volume=20,
        titrant_volume_unit="mL",
        titrant_molarity=0.1,
        analyte_coefficient=1,
        titrant_coefficient=2,
    )
    assert result.analyte_molarity == pytest.approx(0.1)


def test_liter_input_is_supported():
    result = calculate_analyte_concentration(
        analyte_volume=0.025,
        analyte_volume_unit="L",
        titrant_volume=0.0236,
        titrant_volume_unit="L",
        titrant_molarity=0.1,
    )
    assert result.analyte_volume_l == pytest.approx(0.025)
    assert result.analyte_molarity == pytest.approx(0.0944)


def test_average_repeated_measurements():
    assert average([23.5, 23.6, 23.7]) == pytest.approx(23.6)


def test_invalid_unit_is_rejected():
    with pytest.raises(CalculationError, match="mL hoặc L"):
        calculate_analyte_concentration(
            analyte_volume=25,
            analyte_volume_unit="cm3",
            titrant_volume=23.6,
            titrant_volume_unit="mL",
            titrant_molarity=0.1,
        )
