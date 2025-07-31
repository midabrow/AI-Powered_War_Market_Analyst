from fastapi import APIRouter, UploadFile, File
import os
import shutil
from pydantic import BaseModel, Field
from src.services.rag_service import ask_question, build_index
from src.rag.retriever import Retriever
from src.rag.rag_pipeline import RAGPipeline
from src.llm.llm_client import OpenRouterLLMClient
from src.rag.vector_store import VectorStoreBuilder
from src.rag.settings import DATA_DIR

router = APIRouter(prefix="/rag")

class RAGQuery(BaseModel):
    question: str = Field(..., description="Question to ask the RAG system")

retriever = Retriever()
llm = OpenRouterLLMClient()
pipeline = RAGPipeline(retriever, llm)

def ask_question(question: str) -> str:
    return pipeline.ask(question)

def build_index(csv_path: str) -> None:
    builder = VectorStoreBuilder()
    builder.build(csv_path, f"{DATA_DIR}/faiss_store")

@router.post("/ask")
async def ask_rag(query: RAGQuery):
    answer = ask_question(query.question)
    return {"answer": answer}

@router.post("/build-index")
def trigger_index_build(file: UploadFile = File(...)):
    temp_path = "data/temp_uploaded.csv"

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    build_index(temp_path)

    os.remove(temp_path)

    return {"status": "index built from uploaded file"}







