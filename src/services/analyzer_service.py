from src.llm.llm_client import OpenRouterLLMClient

client = OpenRouterLLMClient()

def analyze_event(title: str, sector: str) -> str:
    return client.analyze_event(title, sector)
