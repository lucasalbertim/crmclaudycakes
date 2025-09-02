import requests
import os

def send_whatsapp(phone: str, message: str) -> bool:
    # Exemplo usando Z-API (https://z-api.io/docs/)
    zapi_url = os.getenv("ZAPI_URL")  # Ex: https://api.z-api.io/instances/{instance_id}/token/{token}/send-text
    instance_id = os.getenv("ZAPI_INSTANCE_ID")
    token = os.getenv("ZAPI_TOKEN")
    url = f"https://api.z-api.io/instances/{instance_id}/token/{token}/send-text"
    payload = {
        "phone": phone,
        "message": message
    }
    try:
        response = requests.post(url, json=payload)
        return response.status_code == 200
    except Exception as e:
        print(f"Erro ao enviar WhatsApp: {e}")
        return False
