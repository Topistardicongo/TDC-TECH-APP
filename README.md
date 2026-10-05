# TDC TECH WhatsApp Bot

Official auto-reply for the TDC TECH business number.

## What it does

When a client sends any message (including Hi), the bot **introduces itself immediately**:

```
TDC TECH®
Founded by Topistar Di Congo under TDC CREATIVES.
...
Choose your language:
1 English
2 Français
3 Kiswahili
```

Then: services, payment, inquiry, human agent, refund, feedback, track order, FAQ.

Services and prices match the TDC Tech dashboard (music distribution £15, verification £250, virtual numbers from £2, etc.).

## Deploy

1. Copy `.env.example` to `.env` and fill:
   - `WHATSAPP_TOKEN` from Meta developers
   - `WHATSAPP_PHONE_ID` for +256 751 365093
   - `ADMIN_WHATSAPP` = your personal number (e.g. 256784323850)

2. Install and run:
```bash
pip install -r requirements.txt
python bot.py
```

Or with gunicorn:
```bash
gunicorn -b 0.0.0.0:8080 bot:app
```

3. In Meta app → WhatsApp → Configuration:
   - Callback URL: `https://YOUR-DOMAIN/webhook`
   - Verify token: `tdctech-verify`
   - Subscribe to **messages**

4. Test: send **Hi** to +256 751 365093 from another phone.

## Files

- `bot.py` — the bot
- `leads.json` — created automatically (orders, payments, feedback)
- `sessions.json` — created automatically (chat state)
