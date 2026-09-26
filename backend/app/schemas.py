from typing import Literal

from pydantic import BaseModel, Field


class TitrationCalculationRequest(BaseModel):
    analyte_volume: float = Field(gt=0, description="Thể tích mẫu")
    analyte_volume_unit: Literal["mL", "L", "ml", "l"] = "mL"
    titrant_volume: float = Field(gt=0, description="Thể tích dung dịch chuẩn độ")
    titrant_volume_unit: Literal["mL", "L", "ml", "l"] = "mL"
    titrant_molarity: float = Field(gt=0, description="Nồng độ mol dung dịch chuẩn độ")
    analyte_coefficient: float = Field(default=1, gt=0)
    titrant_coefficient: float = Field(default=1, gt=0)


class TitrationCalculationResponse(BaseModel):
    analyte_molarity: float
    analyte_moles: float
    titrant_moles: float
    formula: str
    steps: list[str]
