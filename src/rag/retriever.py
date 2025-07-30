# src/rag/retriever.py
from sentence_transformers import SentenceTransformer
import faiss
import pickle
import numpy as np
import os



FAISS_INDEX_PATH = "/app/data/faiss_store.index"

VECTOR_STORE_PATH = "/app/data/faiss_store.pkl"

def retrieve_context(question: str, k: int = 5):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    question_vec = model.encode([question])

    index = faiss.read_index(FAISS_INDEX_PATH)
    with open(VECTOR_STORE_PATH, "rb") as f:
        df = pickle.load(f)

    distances, indices = index.search(np.array(question_vec), k)
    return df.iloc[indices[0]]
