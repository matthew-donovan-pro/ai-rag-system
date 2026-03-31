"""Vector store for the AI RAG demo.

Implements a simple in‑memory TF‑IDF vectoriser using scikit‑learn.
"""

from __future__ import annotations

from typing import List, Tuple

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


class VectorStore:
    """A basic TF‑IDF vector store.

    This class holds document embeddings and supports similarity
    search.  It is not optimised for large corpora.
    """

    def __init__(self, documents: List[str]) -> None:
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.matrix = self.vectorizer.fit_transform(documents)

    def query(self, query_text: str, top_k: int = 3) -> Tuple[np.ndarray, np.ndarray]:
        """Compute similarity scores for a query.

        Returns the indices of the top documents and their scores.
        """
        query_vec = self.vectorizer.transform([query_text])
        scores = (self.matrix * query_vec.T).toarray().ravel()
        if top_k <= 0:
            top_k = len(scores)
        # Get indices of top scores
        top_indices = np.argsort(scores)[::-1][:top_k]
        return top_indices, scores[top_indices]


__all__ = ["VectorStore"]