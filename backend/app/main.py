from fastapi import FastAPI
from pathlib import Path

from .calculator import CalculationError, calculate_analyte_concentration
from .document_store import DocumentStore
from .schemas import TitrationCalculationRequest, TitrationCalculationResponse
from .schemas import DocumentSearchRequest, DocumentSearchResponse, DocumentSearchResult


app = FastAPI(
    title="AI Tra Cứu Chuẩn Độ",
    description="API nền tảng cho tra cứu tài liệu và tính toán chuẩn độ.",
    version="0.1.0",
)
document_store = DocumentStore(Path(__file__).parents[3] / "documents")
document_store.reload()


@app.get("/health", tags=["system"])
def health_check() -> dict[str, str]:
    """Return a small readiness response for local development and deployment checks."""
    return {"status": "ok", "service": "ai-tra-cuu-chuan-do"}


@app.post("/api/v1/documents/search", response_model=DocumentSearchResponse, tags=["documents"])
def search_documents(payload: DocumentSearchRequest) -> DocumentSearchResponse:
    """Find relevant document chunks for a future AI/RAG answer."""
    matches = document_store.search(payload.query, payload.limit)
    return DocumentSearchResponse(
        query=payload.query,
        results=[
            DocumentSearchResult(source=item.source, chunk_id=item.chunk_id, text=item.text)
            for item in matches
        ],
    )


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
