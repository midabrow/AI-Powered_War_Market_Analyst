# src/rag/vector_store.py

import pandas as pd
import numpy as np
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from .settings import MODEL_NAME

class VectorStoreBuilder:
    def __init__(self, model_name: str = MODEL_NAME):
        self.model = SentenceTransformer(model_name)

    def build(self, csv_path: str, output_path: str):
        df = pd.read_csv(csv_path)
        df["text"] = df["title"].fillna("") + ". " + df["analysis"].fillna("")
        embeddings = self.model.encode(df["text"].tolist(), show_progress_bar=True)

        index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(np.array(embeddings))
        faiss.write_index(index, f"{output_path}.index")

        with open(f"{output_path}.pkl", "wb") as f:
            pickle.dump(df, f)
