from pathlib import Path

from .rag import DocumentChunk, load_documents, search_documents


class DocumentStore:
    def __init__(self, directory: Path):
        self.directory = directory
        self.chunks: list[DocumentChunk] = []

    def reload(self) -> int:
        self.chunks = load_documents(self.directory)
        return len(self.chunks)

    def search(self, query: str, limit: int = 5) -> list[DocumentChunk]:
        return search_documents(self.chunks, query, limit)
