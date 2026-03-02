import core.config as config

def get_model(chave_complexidade: str) -> str:
    """
    Roteador de modelos baseado em complexidade.
    Retorna o identificador do modelo real a partir das configurações.
    """
    # Verificar se chave_complexidade existe em config.ALLOWED_MODELS
    if chave_complexidade in config.ALLOWED_MODELS:
        return config.ALLOWED_MODELS[chave_complexidade]
    
    # Se não existir, retornar o modelo padrão
    return config.DEFAULT_MODEL
