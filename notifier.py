import requests
from config import TELEGRAM_TOKEN, CHAT_ID

def send_telegram_message(message):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        print("Telegram message skipped (missing TOKEN or CHAT_ID).")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        response = requests.post(url, data=payload, timeout=10)
        response.raise_for_status()
        print("Telegram message sent.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send Telegram message: {e}")
