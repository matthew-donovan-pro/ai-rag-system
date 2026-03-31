"""Query handler for the AI RAG demo.

This module provides a function to search for relevant documents
and format the results for display.
"""

from __future__ import annotations

from typing import List, Tuple

from .retrieval_engine import RetrievalEngine


def handle_query(engine: RetrievalEngine, query: str, top_k: int = 3) -> List[Tuple[str, float]]:
    """Return top documents for a query using the given engine.
    """
    return engine.search(query, top_k)


__all__ = ["handle_query"]