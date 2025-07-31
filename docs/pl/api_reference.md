# 📡 api_reference.md – Endpointy FastAPI


| Endpoint           | Metoda | Opis                                                |
| ------------------ | ------ | --------------------------------------------------- |
| `/classify`        | POST   | Klasyfikuje wydarzenie na typ (atak, sankcja, itp.) |
| `/map_sector`      | POST   | Mapuje wydarzenie do sektora rynku                  |
| `/analyze`         | POST   | Generuje analizę wpływu wydarzenia na sektor        |
| `/rag/ask`         | POST   | Pyta RAG o odpowiedź na zadane pytanie              |
| `/rag/build-index` | POST   | Buduje indeks wektorowy na podstawie pliku CSV      |

### POST /classify

**Opis**: Klasyfikuje wydarzenie (atak, sankcja, itp.)

#### Wejście:

```json
{
  "title": "Ukraine attacked by drones",
  "summary": "Kyiv under fire",
  "link": "http://example.com"
}
```

#### Wyjście:

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

**Opis**: Mapuje wydarzenie do sektora rynku

#### Wejście:

```json
{
  "title": "Ukraine attacked by drones",
  "tag": "attack"
}
```

#### Wyjście:

```json
{
  "sector": "defense"
}
```


### POST /analyze

**Opis**: Generuje analizę ekonomiczną przy użyciu LLM

#### Wejście:

```json
{
  "title": "Ukraine attacked by drones",
  "sector": "defense"
}
```

#### Wyjście:

```json
{
  "analysis": "The attack is likely to increase defense spending..."
}
```


### POST /rag/ask

**Opis**: RAG pipeline: zadanie pytania opartym o wektorową bazę kontekstu

#### Wejście:

```json
{
  "question": "How did recent drone attacks affect oil prices?"
}
```

#### Wyjście:

```json
{
  "answer": "Based on recent events, oil prices increased due to..."
}
```


### POST /rag/build-index

**Opis**: Buduje indeks wektorowy na podstawie CSV

#### Wejście: `multipart/form-data` z plikiem CSV

#### Wyjście:

```json
{
  "status": "index built from uploaded file"
}
```