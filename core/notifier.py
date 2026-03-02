import integrations.telegram_service as telegram_service

def notify_success(task_data: dict, file_name: str):
    """
    Monta e envia notificação de sucesso via Telegram.
    """
    chat_id = task_data.get("chat_id")
    numero_processo = task_data.get("numero_processo")
    
    mensagem = f"Processo {numero_processo} finalizado com sucesso.\nArquivo: {file_name}"
    
    telegram_service.send_message(chat_id, mensagem)

def notify_failure(task_data: dict, erro: str):
    """
    Monta e envia notificação de falha via Telegram.
    """
    chat_id = task_data.get("chat_id")
    numero_processo = task_data.get("numero_processo")
    
    mensagem = f"Erro no processo {numero_processo}.\nDetalhes: {erro}"
    
    telegram_service.send_message(chat_id, mensagem)
