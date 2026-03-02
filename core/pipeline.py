import llm.draft as draft

def generate_minuta(task_data: dict, template_content: str, modelo_real: str) -> str:
    """
    Invólucro simples para geração de minuta via LLM.
    Atua como um componente puro de execução no pipeline.
    """
    # Chamar llm.draft com os parâmetros fornecidos
    texto_gerado = draft.generate(task_data, template_content, modelo_real)
    
    # Retornar o texto gerado diretamente
    return texto_gerado
