from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import os

model_path = os.path.abspath("models/transformer_model")
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)
model.eval()
LABELS = model.config.id2label

def classify_news(input_data) -> dict:
    text = f"{input_data.title} {input_data.summary}"
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1).squeeze()
        pred_id = torch.argmax(probs).item()
        tag = LABELS[pred_id]
        confidence = probs[pred_id].item()

    return {
        "tag": tag,
        "confidence": round(confidence, 4),
        "title": input_data.title,
        "summary": input_data.summary,
        "link": input_data.link
    }
