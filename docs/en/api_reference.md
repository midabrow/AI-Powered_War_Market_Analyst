# 📡 api\_reference.md – FastAPI Endpoints

| Endpoint           | Method | Description                                            |
| ------------------ |--------|--------------------------------------------------------|
| `/classify`        | POST   | Classifies an event into a type (attack, sanction, etc.) |
| `/map_sector`      | POST   | Maps an event to a market sector                        |
| `/analyze`         | POST   | Generates an analysis of the event's impact on a sector |
| `/rag/ask`         | POST   | Asks RAG a question based on recent events              |
| `/rag/build-index` | POST   | Builds a vector index from a CSV file                   |


### POST /classify

**Description**: Classifies an event (e.g. attack, sanctions, etc.)

#### Input:

```json
{
  "title": "Ukraine attacked by drones",
  "summary": "Kyiv under fire",
  "link": "http://example.com"
}
```

#### Output:

```json
{
  "tag": "attack",
  "confidence": 0.9743,
  "title": "...",
  "summary": "...",
  "link": "..."
}
```


### POST /map\_sector

**Description**: Maps an event to a relevant market sector

#### Input:

```json
{
  "title": "Ukraine attacked by drones",
  "tag": "attack"
}
```

#### Output:

```json
{
  "sector": "defense"
}
```


### POST /analyze

**Description**: Generates an economic analysis using an LLM

#### Input:

```json
{
  "title": "Ukraine attacked by drones",
  "sector": "defense"
}
```

#### Output:

```json
{
  "analysis": "The attack is likely to increase defense spending..."
}
```


### POST /rag/ask

**Description**: RAG pipeline: ask a question based on a vectorized context database

#### Input:

```json
{
  "question": "How did recent drone attacks affect oil prices?"
}
```

#### Output:

```json
{
  "answer": "Based on recent events, oil prices increased due to..."
}
```


### POST /rag/build-index

**Description**: Builds a vector index from a CSV file

#### Input: `multipart/form-data` with a CSV file

#### Output:

```json
{
  "status": "index built from uploaded file"
}
```


