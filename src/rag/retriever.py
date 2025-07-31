# src/rag/retriever.py

import faiss
import pickle
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from .settings import MODEL_NAME, INDEX_PATH, STORE_PATH

class Retriever:
    def __init__(self, model_name: str = MODEL_NAME, index_path: str = INDEX_PATH, store_path: str = STORE_PATH):
        self.model = SentenceTransformer(model_name)
        self.index = faiss.read_index(index_path)

        with open(store_path, "rb") as f:
            self.df = pickle.load(f)

    def retrieve(self, question: str, k: int = 5) -> pd.DataFrame:
        query_vec = self.model.encode([question])
        distances, indices = self.index.search(np.array(query_vec), k)
        return self.df.iloc[indices[0]]
