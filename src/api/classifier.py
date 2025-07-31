from fastapi import APIRouter
from pydantic import BaseModel, Field
from src.services.classifier_service import classify_news

router = APIRouter()

class TextInput(BaseModel):
    title: str = Field(..., description="Title of the news article")
    summary: str = Field(..., description="Summary of the news article")
    link: str = Field(..., description="Link to the news article")

@router.post("/classify")
def classify_text(input_data: TextInput) -> dict:
    return classify_news(input_data)
