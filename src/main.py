import os
from dotenv import load_dotenv
from src.llm import LLMClient

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
llm_client = LLMClient(api_key)
