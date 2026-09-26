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


class DocumentSearchRequest(BaseModel):
    query: str = Field(min_length=1, max_length=1000)
    limit: int = Field(default=5, ge=1, le=20)


class DocumentSearchResult(BaseModel):
    source: str
    chunk_id: int
    text: str


class DocumentSearchResponse(BaseModel):
    query: str
    results: list[DocumentSearchResult]
