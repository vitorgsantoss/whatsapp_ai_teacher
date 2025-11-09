import requests
from tools.config import (
    EVOLUTION_API_URL,
    EVOLUTION_INSTANCE_NAME,
    EVOLUTION_AUTHENTICATION_API_KEY
)


def send_whatsapp_message(group_id, text):
    url = f"{EVOLUTION_API_URL}/message/sendText/{EVOLUTION_INSTANCE_NAME}"
    headers = {
        "apikey": EVOLUTION_AUTHENTICATION_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "number": group_id,
        "text": text
    }
    requests.post(
        url=url,
        json=payload,
        headers=headers
    )
