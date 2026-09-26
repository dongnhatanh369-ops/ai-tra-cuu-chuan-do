from pathlib import Path

from backend.app.rag import load_documents, search_documents


def test_loads_and_searches_vietnamese_document(tmp_path: Path):
    (tmp_path / "axit-bazo.md").write_text(
        "Chuẩn độ axit bazơ dùng để xác định nồng độ dung dịch. Chỉ thị đổi màu tại điểm tương đương.",
        encoding="utf-8",
    )
    chunks = load_documents(tmp_path, chunk_size=100)
    results = search_documents(chunks, "điểm tương đương chỉ thị")
    assert results
    assert results[0].source == "axit-bazo.md"


def test_ignores_unsupported_files(tmp_path: Path):
    (tmp_path / "image.pdf").write_bytes(b"not indexed yet")
    assert load_documents(tmp_path) == []
