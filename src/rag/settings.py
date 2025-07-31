# src/rag/settings.py

import os

DATA_DIR = os.getenv("RAG_DATA_DIR", "/app/data")
INDEX_PATH = os.path.join(DATA_DIR, "faiss_store.index")
STORE_PATH = os.path.join(DATA_DIR, "faiss_store.pkl")
MODEL_NAME = "all-MiniLM-L6-v2"
