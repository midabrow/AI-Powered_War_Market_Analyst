# src/rag/rag_client.py
import requests
from .retriever import retrieve_context

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")


# https://openrouter.ai/docs/quickstart#chat-completions
# https://openrouter.ai/google/gemma-3-4b-it:free/api
def ask_question_rag(question: str) -> str:
    context_df = retrieve_context(question)
    context_text = "\n".join(
        f"- {row['title']}: {row['analysis']}" for _, row in context_df.iterrows()
    )

    prompt = (
        f"Answer the question based on the following recent geopolitical events:\n\n"
        f"{context_text}\n\n"
        f"Question: {question}\n\nAnswer:"
    )

    payload = {
        "model": "google/gemma-3-4b-it:free",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    if not API_KEY:
        raise RuntimeError("❌ OPENROUTER_API_KEY is not set!")


    response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload, headers=headers)

    # Debug log
    print("🔍 RESPONSE", response.status_code, response.text)
    try:
        result = response.json()
    except Exception as e:
        raise RuntimeError(f"❌ Failed to parse response: {response.text}") from e

    if "choices" not in result:
        raise ValueError(f"❌ Unexpected response from OpenRouter:\n{result}")

    return response.json()["choices"][0]["message"]["content"]

