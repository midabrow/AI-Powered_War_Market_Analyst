# 🤖 models.md – Model klasyfikacji

## Architektura

* Model bazuje na `bert-base-uncased`
* Fine-tuning wykonany na zbiorze `tagged_balanced.csv`
* Liczba klas: 5 (attack, sanction, escalation, deescalation, other)

## Dane treningowe

* Łącznie \~2000 rekordów z RSS Reutersa
* Zrównoważone klasy
* Przykładowe pola: `title`, `summary`, `label`

## Metryki (val set)

* Accuracy: 0.91
* F1-macro: 0.88

## Eksport

* Model zapisany w `models/transformer_model/`
* Format: HuggingFace + `model.safetensors`