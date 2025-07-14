from fastapi import FastAPI
from pydantic import BaseModel
from src.classification.model import NewsClassifier
from src.mapping.sector_mapper import SectorMapper
from src.llm.llm_client import LLMClient
from typing import Union, List
import os

app = FastAPI()
classifier = NewsClassifier()

# Training data — minimal working dataset
TRAIN_TEXTS = [
    "Russia launches missile strike on Kyiv",
    "US imposes sanctions on Iran",
    "NATO supplies weapons to Ukraine",
    "Tensions escalate near Taiwan",
    "Drone incident reported in Syria",
]
TRAIN_TAGS = [
    "attack",
    "sanction",
    "supply",
    "escalation",
    "incident"
]

classifier.train(TRAIN_TEXTS, TRAIN_TAGS)

class InputText(BaseModel):
    text: str

@app.post("/classify")
def classify_event(item: InputText):
    """
    Predict the tag for a given event title/teaser.
    """
    tag = classifier.predict(item.text)
    return {"tag": tag}




sector_mapper = SectorMapper()
llm = LLMClient(api_key=os.getenv("OPENROUTER_API_KEY"))


# 🔣 Model wejściowy
class AnalyzeRequest(BaseModel):
    title: str
    content: str

# 🚀 Endpoint główny
@app.post("/analyze")
def analyze_event(req: AnalyzeRequest):
    """
    Full pipeline: classify → map sectors → generate LLM analysis
    """
    full_text = f"{req.title} {req.content}"
    tag = classifier.predict(full_text)
    sectors = sector_mapper.map_to_sector(full_text)

    results = []

    for sector in sectors:
        try:
            analysis = llm.generate_analysis(full_text, sector)
        except Exception as e:
            analysis = f"[ERROR] {str(e)}"
        results.append({
            "sector": sector,
            "analysis": analysis
        })

    return {
        "title": req.title,
        "content": req.content,
        "tag": tag,
        "sectors": sectors,
        "analyses": results
    }