from fastapi import FastAPI

from .calculator import CalculationError, calculate_analyte_concentration
from .schemas import TitrationCalculationRequest, TitrationCalculationResponse


app = FastAPI(
    title="AI Tra Cứu Chuẩn Độ",
    description="API nền tảng cho tra cứu tài liệu và tính toán chuẩn độ.",
    version="0.1.0",
)


@app.get("/health", tags=["system"])
def health_check() -> dict[str, str]:
    """Return a small readiness response for local development and deployment checks."""
    return {"status": "ok", "service": "ai-tra-cuu-chuan-do"}


@app.post("/api/v1/titration/calculate", response_model=TitrationCalculationResponse, tags=["titration"])
def calculate_titration(payload: TitrationCalculationRequest) -> TitrationCalculationResponse:
    """Calculate analyte molarity at the equivalence point."""
    try:
        result = calculate_analyte_concentration(**payload.model_dump())
    except CalculationError as error:
        from fastapi import HTTPException

        raise HTTPException(status_code=422, detail=str(error)) from error

    return TitrationCalculationResponse(
        analyte_molarity=result.analyte_molarity,
        analyte_moles=result.analyte_moles,
        titrant_moles=result.titrant_moles,
        formula="C_A × V_A / a = C_B × V_B / b",
        steps=[
            f"V_A = {result.analyte_volume_l} L; V_B = {result.titrant_volume_l} L.",
            "Tính số mol dung dịch chuẩn độ: n_B = C_B × V_B.",
            "Dùng tỉ lệ hệ số phản ứng để tính số mol chất phân tích.",
            "Tính nồng độ chất phân tích: C_A = n_A / V_A.",
        ],
    )
