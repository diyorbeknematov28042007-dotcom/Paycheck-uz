# Payment Verification Telegram Bot

Stack:
- Python
- Aiogram 3
- FastAPI
- PostgreSQL (Neon)
- Railway deploy

## Features
- Uzbek/Russian language
- Welcome post
- Payment verification flow
- Screenshot upload
- Admin broadcast
- Payment history
- Settings
- Persistent users via Telegram ID

## Setup

```bash
pip install -r requirements.txt
```

Create `.env`

```env
BOT_TOKEN=YOUR_BOT_TOKEN
DATABASE_URL=YOUR_NEON_URL
ADMIN_IDS=123456789
GROUP_ID=-100123456789
```

Run:

```bash
python main.py
```