# 🛠 setup.md – Installation and Launch

## Prerequisites

* Docker + Docker Compose
* OpenRouter account (API key for LLM)
* Google account + Google Sheets
* Telegram account + bot token
* Ngrok account for webhook tunneling


## Installation

1. Clone the repository:

```bash
git clone https://github.com/midabrow/AI-Powered_War_Market_Analyst
cd AI-Powered_War_Market_Analyst
```

2. Configure environment variables:
   Create a `.env` file based on `.env.example` and fill in the following:

```
OPENROUTER_API_KEY=...
GOOGLE_SHEETS_ID=...
TELEGRAM_BOT_TOKEN=...

# The public URL where n8n exposes its webhooks
WEBHOOK_URL=https://helping-capital-chicken.ngrok-free.app

# Host address (without protocol)
N8N_HOST=helping-capital-chicken.ngrok-free.app

# Protocol to use (http/https)
N8N_PROTOCOL=https

# Token from https://dashboard.ngrok.com/get-started/your-authtoken
NGROK_TOKEN=...

# API Key from https://openrouter.ai/settings/keys
OPENROUTER_API_KEY=...
```

3. Launch the application:

```bash
docker compose up --build
```

4. (Optional) Tunnel Telegram webhook using ngrok:

```bash
ngrok http 8000
```

Then register the webhook:

```bash
https://api.telegram.org/bot<token>/setWebhook?url=https://your-url.ngrok.io/webhook
```


## Testing

```bash
docker compose run --rm tests
```


