# src/rag/rag_pipeline.py

from src.rag.retriever import Retriever
from src.llm.llm_client import OpenRouterLLMClient

class RAGPipeline:
    def __init__(self, retriever: Retriever, llm_client: OpenRouterLLMClient):
        self.retriever = retriever
        self.llm_client = llm_client

    def ask(self, question: str) -> str:
        context_df = self.retriever.retrieve(question)
        context_text = "\n".join(
            f"- {row['title']}: {row['analysis']}"
            for _, row in context_df.iterrows()
        )

        prompt = (
            f"Answer the question based on the following recent geopolitical events:\n\n"
            f"{context_text}\n\n"
            f"Question: {question}\n\nAnswer:"
        )

        return self.llm_client.ask(prompt)
