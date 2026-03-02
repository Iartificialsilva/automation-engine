def validate_all(texto_gerado: str, task_data: dict) -> bool:
    """
    Validador estrutural determinístico para minutas jurídicas.
    Verifica integridade básica, ausência de placeholders e presença de dados críticos.
    """
    # 1. Se texto_gerado for None ou string vazia → retornar False
    if not texto_gerado or not isinstance(texto_gerado, str):
        return False

    # 2. Se o texto contiver “{{” ou “}}” → retornar False
    if "{{" in texto_gerado or "}}" in texto_gerado:
        return False

    # 3. Se numero_processo não estiver presente em task_data → retornar False
    if "numero_processo" not in task_data or not task_data["numero_processo"]:
        return False

    # 4. Se task_data["numero_processo"] não aparecer dentro de texto_gerado → retornar False
    if str(task_data["numero_processo"]) not in texto_gerado:
        return False

    # 5. Se o tamanho do texto for menor que 500 caracteres → retornar False
    if len(texto_gerado) < 500:
        return False

    # 6. Se todas as validações passarem → retornar True
    return True
