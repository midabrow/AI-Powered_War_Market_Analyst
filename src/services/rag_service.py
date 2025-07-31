# services/rag_service.py

from src.rag.retriever import Retriever
from src.rag.rag_pipeline import RAGPipeline
from src.llm.llm_client import OpenRouterLLMClient
from src.rag.vector_store import VectorStoreBuilder
from src.rag.settings import DATA_DIR

retriever = Retriever()
llm = OpenRouterLLMClient()
pipeline = RAGPipeline(retriever, llm)

def ask_question(question: str) -> str:
    return pipeline.ask(question)

def build_index(csv_path: str) -> None:
    builder = VectorStoreBuilder()
    builder.build(csv_path, f"{DATA_DIR}/faiss_store")
