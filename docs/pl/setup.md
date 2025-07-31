# 🛠 setup.md – Instalacja i uruchomienie

## Wymagania wstępne

* Docker + Docker Compose
* Konto OpenRouter (klucz API do LLM)
* Konto Google + arkusz Google Sheets
* Konto Telegram + Token bota
* Konto na ngrok do webhooków

## Instalacja

1. Sklonuj repozytorium:

```bash
git clone https://github.com/midabrow/AI-Powered_War_Market_Analyst
cd AI-Powered_War_Market_Analyst
```

2. Skonfiguruj zmienne środowiskowe:
   Stwórz plik `.env` na podstawie `.env.example` i uzupełnij:

```
OPENROUTER_API_KEY=...
GOOGLE_SHEETS_ID=...
TELEGRAM_BOT_TOKEN=...
#  Adres, pod którym n8n wystawia swoje webhooki
WEBHOOK_URL=https://helping-capital-chicken.ngrok-free.app

# Adres hosta (bez protokołu) 
N8N_HOST=helping-capital-chicken.ngrok-free.app

# Protokół do użycia (http/https)
N8N_PROTOCOL=https

# Token z https://dashboard.ngrok.com/get-started/your-authtoken
NGROK_TOKEN=...

# API Key z https://openrouter.ai/settings/keys
OPENROUTER_API_KEY=...
```

3. Uruchom aplikację:

```bash
docker compose up --build
```

4. (Opcjonalnie) Tunel webhooka Telegrama przez ngrok:

```bash
ngrok http 8000
```

I zarejestruj webhook:

```bash
https://api.telegram.org/bot<token>/setWebhook?url=https://twój-url.ngrok.io/webhook
```

## Testowanie:

```bash
docker compose run --rm tests
```