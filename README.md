# AI Document Retrieval System (RAG)

This repository demonstrates a simplified retrieval-augmented generation (RAG) system designed to illustrate how document search and semantic retrieval pipelines operate in applied AI systems.

The implementation uses lightweight techniques (TF-IDF and cosine similarity) to clearly expose the core mechanics behind retrieval systems without relying on external APIs or large-scale infrastructure.

---

## Overview

The system ingests a small corpus of documents, builds a vector representation, and retrieves the most relevant documents for a given query.

It demonstrates the fundamental stages of a RAG pipeline:

- document ingestion  
- text vectorisation  
- similarity-based retrieval  
- ranked result output  

This is a **structural demonstration of RAG**, not a production implementation.

---

## System Components

- **Document Pipeline**  
  Loads and preprocesses plain-text documents from a local corpus

- **Vectorisation Layer**  
  TF-IDF transformation of document text into vector space representations

- **Similarity Engine**  
  Cosine similarity used to compare query vectors against document vectors

- **Retrieval Layer**  
  Returns ranked documents based on similarity scores

- **Query Interface**  
  Command-line interface for executing search queries

---

## Architecture

The system follows a simplified retrieval pipeline:

1. Document ingestion from local files  
2. Text preprocessing and tokenisation  
3. TF-IDF vector generation  
4. Query vector transformation  
5. Cosine similarity scoring  
6. Ranked document retrieval  

This structure mirrors production RAG systems where TF-IDF would typically be replaced with embedding models and vector databases.

---

## Features

- Document ingestion from local corpus  
- Vectorisation using TF-IDF  
- Similarity search using cosine distance  
- Ranked retrieval with similarity scoring  
- Clear separation of ingestion, indexing, and retrieval stages  

---

## Quick Start

Install dependencies:

```bash
pip install -r requirements.txt
