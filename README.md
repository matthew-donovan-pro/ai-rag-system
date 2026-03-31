# AI Document Analysis System (RAG)

This repository demonstrates a simple retrieval‑augmented generation (RAG) system.  It reads a small corpus of text files, builds an in‑memory vector store using TF‑IDF and cosine similarity, and returns the most relevant documents for a given query.

**Important**: This is a demonstration only.  It uses simplified logic and a tiny corpus.  Production RAG systems use more sophisticated embedding models, chunking strategies and back‑end storage.

## Features

- **Document ingestion** – load plain‑text files from `data/documents/`.
- **Vector store** – build a term frequency matrix and compute cosine similarity.
- **Retrieval** – find the top matching documents for a given query.

## Quick start

1. Install dependencies (only standard library required in this demo):

   ```bash
   pip install -r requirements.txt
   ```

2. Run the demo script:

   ```bash
   python demo/run_rag_demo.py --query "example search"
   ```

   The script prints the top matching documents and their similarity scores.

## Notes on IP

This demonstration is intentionally simple and uses trivial TF‑IDF logic.  Production systems typically employ transformer embeddings, chunking and external vector databases.