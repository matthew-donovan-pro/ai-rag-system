#!/usr/bin/env python3
"""Run a simple retrieval‑augmented generation demo.

Reads a small corpus of documents, builds a TF‑IDF vector store and
prints the top matching documents for a given query.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.retrieval_engine import RetrievalEngine  # type: ignore


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="AI RAG demo")
    parser.add_argument("--query", required=True, help="Query text to search for")
    parser.add_argument("--top_k", type=int, default=3, help="Number of top documents to return")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    data_dir = Path(__file__).resolve().parents[1] / "data" / "documents"
    engine = RetrievalEngine(str(data_dir))
    results = engine.search(args.query, args.top_k)
    print(f"Top {len(results)} documents for query: '{args.query}'")
    for filename, score in results:
        print(f"{filename} – score: {score:.4f}")


if __name__ == "__main__":
    main()