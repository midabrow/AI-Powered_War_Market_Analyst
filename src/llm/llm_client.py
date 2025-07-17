import requests
from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


def analyze_event(title: str, sector: str) -> Optional[str]:
    """
    Sends prompt to LLM and returns response about economic impact.
    """
    prompt = (
        f"Event: {title}\n"
        f"How could this event affect the {sector} sector?\n"
        f"Give a short economic impact analysis in plain English."
    )

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "mistralai/mixtral-8x7b-instruct",
        "messages": [
            {"role": "system", "content": "You are an expert economic analyst."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 200,
        "temperature": 0.7,
    }

    try:
        response = requests.post(OPENROUTER_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"[LLM ERROR] {e}")
        return None
