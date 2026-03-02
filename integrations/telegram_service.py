import requests
import os
import core.config as config

def send_message(chat_id: str, mensagem: str) -> None:
    """
    Envia uma mensagem de texto via API do Telegram (Bot API).
    """
    # 1. Obter token (config -> env -> exception)
    token = config.TELEGRAM_TOKEN
    if not token:
        token = os.getenv("TELEGRAM_TOKEN")
    
    if not token:
        raise Exception("TELEGRAM_TOKEN não configurado")
    
    # 2. Montar URL
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    # 3. Fazer POST
    payload = {
        "chat_id": chat_id,
        "text": mensagem
    }
    
    response = requests.post(url, json=payload)
    
    # 4. Validar status_code
    if response.status_code != 200:
        raise Exception("Erro ao enviar mensagem para o Telegram")
    
    # 5. Não retornar nada
