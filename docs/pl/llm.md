


# 🧠 llm.md – Promptowanie i RAG

## Prompt do analizy wydarzeń

```text
Event: [title]
How could this event affect the [sector] sector?
Give a short economic impact analysis in plain English.
```

* Wysyłany do OpenRouter API (model: `mixtral-8x7b-instruct`)
* Role system: "You are an expert economic analyst."

## Prompt do RAG (`/rag/ask`)

```text
Answer the question based on the following recent geopolitical events:

- Title1: Analysis1
- Title2: Analysis2
...

Question: [question]
Answer:
```

* Łączy dane z FAISS + analizę LLM
* Retrieval: top 5 podobnych wydarzeń

## Model

* OpenRouter z API keyem
* Domyślny model: `mistralai/mixtral-8x7b-instruct`
* Możliwa zmiana na Claude, GPT, Llama itp.
