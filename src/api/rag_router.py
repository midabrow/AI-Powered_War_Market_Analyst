from fastapi import APIRouter, UploadFile, File
import shutil
import os
from pydantic import BaseModel
from src.rag.rag_client import ask_question_rag
from src.rag.embedder import build_vector_store

router = APIRouter()

class RAGQuery(BaseModel):
    question: str

@router.post("/ask")
async def ask_rag(query: RAGQuery):
    answer = ask_question_rag(query.question)
    return {"answer": answer}


@router.post("/build-index")
def trigger_index_build(file: UploadFile = File(...)):
    temp_path = "data/temp_uploaded.csv"

    # Zapisz plik tymczasowo
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Buduj index na podstawie przesłanego pliku
    build_vector_store(temp_path)

    # Usuń tymczasowy plik (opcjonalnie)
    os.remove(temp_path)

    return {"status": "index built from uploaded file"}