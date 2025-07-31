from fastapi import APIRouter
from pydantic import BaseModel, Field
from src.services.analyzer_service import analyze_event

router = APIRouter()

class AnalyzeRequest(BaseModel):
    title: str = Field(..., description="Title of the event to analyze")
    sector: str = Field(..., description="Sector of the event to analyze")

@router.post("/analyze")
def analyze(req: AnalyzeRequest) -> dict:
    return {"analysis": analyze_event(req.title, req.sector)}
