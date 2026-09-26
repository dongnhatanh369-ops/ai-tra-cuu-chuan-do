"""Deterministic calculations for common titration problems."""

from dataclasses import dataclass


class CalculationError(ValueError):
    """Raised when titration input is invalid."""


@dataclass(frozen=True)
class TitrationResult:
    analyte_molarity: float
    analyte_moles: float
    titrant_moles: float
    analyte_volume_l: float
    titrant_volume_l: float


def _positive(name: str, value: float) -> None:
    if value <= 0:
        raise CalculationError(f"{name} phải lớn hơn 0.")


def calculate_analyte_concentration(
    *,
    analyte_volume: float,
    analyte_volume_unit: str,
    titrant_volume: float,
    titrant_volume_unit: str,
    titrant_molarity: float,
    analyte_coefficient: float = 1.0,
    titrant_coefficient: float = 1.0,
) -> TitrationResult:
    """Calculate analyte concentration at the equivalence point.

    For ``a A + b B -> products``: ``n_A / a = n_B / b``.
    Supported volume units are ``mL`` and ``L``.
    """
    for name, value in (
        ("Thể tích chất phân tích", analyte_volume),
        ("Thể tích dung dịch chuẩn độ", titrant_volume),
        ("Nồng độ dung dịch chuẩn độ", titrant_molarity),
        ("Hệ số chất phân tích", analyte_coefficient),
        ("Hệ số dung dịch chuẩn độ", titrant_coefficient),
    ):
        _positive(name, value)

    analyte_volume_l = _to_liters(analyte_volume, analyte_volume_unit)
    titrant_volume_l = _to_liters(titrant_volume, titrant_volume_unit)
    titrant_moles = titrant_molarity * titrant_volume_l
    analyte_moles = titrant_moles * analyte_coefficient / titrant_coefficient

    return TitrationResult(
        analyte_molarity=analyte_moles / analyte_volume_l,
        analyte_moles=analyte_moles,
        titrant_moles=titrant_moles,
        analyte_volume_l=analyte_volume_l,
        titrant_volume_l=titrant_volume_l,
    )


def _to_liters(value: float, unit: str) -> float:
    normalized = unit.strip().lower()
    if normalized == "l":
        return value
    if normalized in {"ml", "mℓ"}:
        return value / 1000
    raise CalculationError("Đơn vị thể tích chỉ được là mL hoặc L.")


def average(values: list[float]) -> float:
    """Return the mean of repeated titration measurements."""
    if not values:
        raise CalculationError("Cần ít nhất một giá trị để tính trung bình.")
    for value in values:
        _positive("Giá trị đo", value)
    return sum(values) / len(values)
