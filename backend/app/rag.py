"""Small, dependency-free document retrieval layer for the first RAG iteration."""

from dataclasses import dataclass
from pathlib import Path
import re


@dataclass(frozen=True)
class DocumentChunk:
    source: str
    chunk_id: int
    text: str
    terms: frozenset[str]


def _terms(text: str) -> frozenset[str]:
    return frozenset(re.findall(r"[\wÀ-ỹ]+", text.lower(), flags=re.UNICODE))


def load_documents(directory: Path, chunk_size: int = 900) -> list[DocumentChunk]:
    """Load Markdown/text documents and split them into searchable chunks."""
    if chunk_size < 100:
        raise ValueError("chunk_size phải từ 100 ký tự trở lên.")
    chunks: list[DocumentChunk] = []
    for path in sorted(directory.glob("**/*")):
        if path.suffix.lower() not in {".txt", ".md"}:
            continue
        text = path.read_text(encoding="utf-8").strip()
        for index, start in enumerate(range(0, len(text), chunk_size)):
            chunk_text = text[start : start + chunk_size].strip()
            if chunk_text:
                chunks.append(DocumentChunk(path.name, index, chunk_text, _terms(chunk_text)))
    return chunks


def search_documents(chunks: list[DocumentChunk], query: str, limit: int = 5) -> list[DocumentChunk]:
    """Return chunks ranked by the number of matching query terms."""
    query_terms = _terms(query)
    if not query_terms:
        return []
    ranked = [(len(query_terms & chunk.terms), chunk) for chunk in chunks]
    ranked = [(score, chunk) for score, chunk in ranked if score > 0]
    ranked.sort(key=lambda item: (-item[0], item[1].source, item[1].chunk_id))
    return [chunk for _, chunk in ranked[:limit]]
