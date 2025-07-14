import requests



class LLMClient:
    """
    Sends prompts to an LLM API (e.g., OpenRouter, OpenAI, etc.) and returns the response.
    """
    def __init__(self, api_key: str, model: str = "openrouter/mistral-7b"):
        self.api_key = api_key
        self.model = model
        self.url = "https://openrouter.ai/api/v1/chat/completions"

    def query(self, event_text: str, sector: str) -> str:
        """
        Generate LLM analysis based on event text and market sector.
        """
        prompt = (
            f"How might the following event affect the {sector} sector?\n\n"
            f"{event_text}\n\n"
            f"Provide a concise, expert-level analysis."
        )
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(self.url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
