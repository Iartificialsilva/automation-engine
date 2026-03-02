from openclaw import OpenClawClient

# Conectar ao OpenClaw local
client = OpenClawClient(
    base_url="http://localhost:18789",  # Porta do seu OpenClaw local
    token="b8c89901621f30b808c6fa8fff2cf2ad460584abc9792374"  # Token do seu openclaw.json
)

def generate(task_data, template_content, modelo_real):
    """
    Gera uma minuta de texto via OpenClaw usando o modelo selecionado.
    """
    # Construir o prompt para o modelo
    prompt = f"{template_content}\n\nDetalhes da tarefa: {task_data}"

    # Chamada para OpenClaw
    response = client.completions.create(
        model=modelo_real,
        input=prompt
    )

    # Retornar o texto gerado
    return response.output_text