# 🤖 models.md – Classification Model

## Architecture

* The model is based on `bert-base-uncased`
* Fine-tuned on the `tagged_balanced.csv` dataset
* Number of classes: 5 (`attack`, `sanction`, `escalation`, `deescalation`, `other`)


## Training Data

* \~2000 records collected from Reuters RSS feeds
* Balanced class distribution
* Sample fields: `title`, `summary`, `label`


## Metrics (validation set)

* Accuracy: 0.91
* F1-macro: 0.88


## Export

* Model saved in `models/transformer_model/`
* Format: HuggingFace + `model.safetensors`



