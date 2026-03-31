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

- Ingests and indexes document corpus using TF-IDF vectorisation
- Performs cosine similarity search across indexed documents
- Returns ranked results with similarity scoring for each query
- Achieves sub-second query response time on small to medium document sets
- Demonstrates retrieval pipeline structure used in production RAG systems 

---

## Demo

Run:

```bash
pip install -r requirements.txt
python demo/run_rag_demo.py --query "example search"
