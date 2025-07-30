from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoConfig
import torch
from src.mapping.sector_mapper import map_to_sector
from src.llm.llm_client import analyze_event
from src.rss.rss_fetcher import fetch_all_rss, rss_dict
from src.api.rag_router import router as rag_router 

import os
app = FastAPI()

# dodatkowy router
app.include_router(rag_router, prefix="/rag")

@app.get("/rss/fetch")
def fetch_articles() -> list[dict]:
    df = fetch_all_rss(rss_dict)
    return df.to_dict(orient="records")


model_path = os.path.abspath("models/transformer_model")
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

model.eval()  


LABELS = model.config.id2label

class TextInput(BaseModel):
    title: str  
    summary: str
    link: str 


@app.post("/classify")
def classify_text(input_data: TextInput) -> dict:
    """
    Classifies a news item using a fine-tuned transformer model.
    Returns predicted tag with score.
    """
    text = f"{input_data.title} {input_data.summary}"
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1).squeeze()
        pred_id = torch.argmax(probs).item()
        tag = LABELS[pred_id]
        confidence = probs[pred_id].item()

    return {"tag": tag, "confidence": round(confidence, 4), "title": input_data.title, "summary": input_data.summary, "link": input_data.link}
    
##############

class MappingRequest(BaseModel):
    title: str
    tag: str

@app.post("/map_sector")
def map_sector(req: MappingRequest) -> dict:
    """
    Assigns sector to the given title + tag.
    """
    sector = map_to_sector(req.title, req.tag)
    return {"sector": sector}

###############

class AnalyzeRequest(BaseModel):
    title: str
    sector: str

@app.post("/analyze")
def analyze(req: AnalyzeRequest) -> dict:
    result = analyze_event(req.title, req.sector)
    return {"analysis": result}