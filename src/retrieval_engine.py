"""Retrieval engine for the AI RAG demo.

Combines document ingestion and vector store to return top
documents for a given query.
"""

from __future__ import annotations

from typing import List, Tuple

from .document_processor import load_documents
from .vector_store import VectorStore


class RetrievalEngine:
    """High‑level retrieval engine.

    Loads documents, builds the vector store and executes queries.
    """

    def __init__(self, doc_dir: str):
        self.docs = load_documents(doc_dir)
        self.store = VectorStore([content for _, content in self.docs])

    def search(self, query: str, top_k: int = 3) -> List[Tuple[str, float]]:
        """Return the filenames and scores of the top documents.
        """
        indices, scores = self.store.query(query, top_k)
        results: List[Tuple[str, float]] = []
        for idx, score in zip(indices, scores):
            filename = self.docs[idx][0]
            results.append((filename, float(score)))
        return results


__all__ = ["RetrievalEngine"]