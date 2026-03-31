"""Document ingestion for the AI RAG system demo.

Reads plain‑text documents from a directory and returns their
contents for further processing.  Production systems typically
include tokenisation, chunking and filtering steps which are
omitted here for simplicity.
"""

from __future__ import annotations

from pathlib import Path
from typing import List, Tuple


def load_documents(directory: str) -> List[Tuple[str, str]]:
    """Load all text files from the given directory.

    Parameters
    ----------
    directory: str
        Path to the directory containing plain‑text files.

    Returns
    -------
    List[Tuple[str, str]]
        A list of (filename, content) tuples.
    """
    docs: List[Tuple[str, str]] = []
    for path in Path(directory).glob("*.txt"):
        try:
            content = path.read_text(encoding="utf-8")
            docs.append((path.name, content))
        except Exception:
            continue
    return docs


__all__ = ["load_documents"]