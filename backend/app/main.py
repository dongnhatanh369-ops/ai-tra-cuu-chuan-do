from fastapi import FastAPI

app = FastAPI(
    title="AI Tra Cứu Chuẩn Độ",
    description="API nền tảng cho tra cứu tài liệu và tính toán chuẩn độ.",
    version="0.1.0",
)


@app.get("/health", tags=["system"])
def health_check() -> dict[str, str]:
    """Return a small readiness response for local development and deployment checks."""
    return {"status": "ok", "service": "ai-tra-cuu-chuan-do"}
