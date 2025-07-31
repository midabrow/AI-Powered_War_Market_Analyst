# src/llm/llm_client.py

import os
import logging
import requests
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


class OpenRouterLLMClient:
    def __init__(self, api_key: Optional[str] = None, model: str = "mistralai/mixtral-8x7b-instruct"):
        self.api_key = api_key or OPENROUTER_API_KEY
        self.model = model
        if not self.api_key:
            raise ValueError("Missing OPENROUTER_API_KEY in environment variables.")

    def _build_headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def _post(self, payload: dict) -> Optional[str]:
        try:
            response = requests.post(OPENROUTER_URL, headers=self._build_headers(), json=payload)
            response.raise_for_status()
            result = response.json()

            if "choices" not in result:
                logger.error(f"Invalid response format from OpenRouter: {result}")
                return None

            return result["choices"][0]["message"]["content"].strip()

        except requests.RequestException as e:
            logger.error(f"[OpenRouter API Error] {e}")
        except Exception as e:
            logger.exception(f"[Unexpected Error] {e}")

        return None

    def analyze_event(self, title: str, sector: str) -> Optional[str]:
        prompt = (
            f"Event: {title}\n"
            f"How could this event affect the {sector} sector?\n"
            f"Give a short economic impact analysis in plain English."
        )

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are an expert economic analyst."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 200,
            "temperature": 0.7,
        }

        return self._post(payload)
    

    def ask(self, prompt: str) -> Optional[str]:
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 300
        }
        return self._post(payload)

