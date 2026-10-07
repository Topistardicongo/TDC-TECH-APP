import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

WHATSAPP_TOKEN = os.environ.get("WHATSAPP_TOKEN")
VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN", "tdc_tech_secret_2026")

@app.route("/webhook", methods=["GET"])
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    
    if mode and token:
        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Verification failed", 403
    return "Hello world", 200

@app.route("/webhook", methods=["POST"])
def receive_message():
    data = request.get_json()
    print("Incoming webhook data:", data)
    try:
        if "object" in data and "entry" in data:
            for entry in data["entry"]:
                for change in entry.get("changes", []):
                    value = change.get("value", {})
                    if "messages" in value:
                        phone_number_id = value["metadata"]["phone_number_id"]
                        from_number = value["messages"][0]["from"]
                        msg_body = value["messages"][0]["text"]["body"]
                        
                        send_reply(phone_number_id, from_number, f"Welcome to TDC TECH! Received: {msg_body}")
    except Exception as e:
        print(f"Error handling message: {e}")
    return jsonify({"status": "success"}), 200

def send_reply(phone_number_id, recipient_number, message_text):
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": recipient_number,
        "type": "text",
        "text": {"body": message_text}
    }
    url = f"https://graph.facebook.com/v18.0/{phone_number_id}/messages"
    response = requests.post(url, json=payload, headers=headers)
    print("WhatsApp API Response:", response.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
