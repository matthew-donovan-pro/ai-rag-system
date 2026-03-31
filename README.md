# AI Document Analysis System (RAG)

**Retrieval-augmented document analysis demo using indexing, similarity search, and structured retrieval workflows.**

---

## Overview

This project demonstrates the core architecture of a retrieval-augmented generation (RAG) system for document analysis.

It shows:
- document ingestion and indexing  
- vector-based similarity search  
- retrieval of relevant content for a given query  

The implementation uses TF-IDF and cosine similarity to make the workflow transparent. In production, this would be replaced with embedding models, chunking strategies, and scalable vector storage.

---

## Features

- **Document ingestion** — loads and processes text files from `data/documents/`  
- **Vector store** — builds a TF-IDF matrix for document representation  
- **Retrieval engine** — performs similarity search using cosine similarity  
- **Query handling** — returns top matching documents with relevance scores  

---

## Demo

Run:

```bash
pip install -r requirements.txt
python demo/run_rag_demo.py --query "example search"
