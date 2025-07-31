# 🧠 llm.md – Prompting and RAG

## Prompt for Event Analysis

```text
Event: [title]
How could this event affect the [sector] sector?
Give a short economic impact analysis in plain English.
```

* Sent to the OpenRouter API (model: `mixtral-8x7b-instruct`)
* System role: "You are an expert economic analyst."


## Prompt for RAG (`/rag/ask`)

```text
Answer the question based on the following recent geopolitical events:

- Title1: Analysis1
- Title2: Analysis2
...

Question: [question]
Answer:
```

* Combines data from FAISS with LLM-based analysis
* Retrieval: top 5 most relevant events


## Model

* Uses OpenRouter with API key
* Default model: `mistralai/mixtral-8x7b-instruct`
* Can be switched to Claude, GPT, LLaMA, etc.

