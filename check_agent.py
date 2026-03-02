from openclaw import OpenClaw

# Token que você atualizou (com cmdop_)
TOKEN = "cmdop_b8c89901621f30b808c6fa8fff2cf2ad460584abc9792374"
SERVER = "localhost:18789"  # host:porta do seu OpenClaw local

# Criar cliente via método remoto
client = OpenClaw.remote(
    api_key=TOKEN,
    server=SERVER,
    insecure=True
)

# Teste rápido do agente
try:
    response = client.agent.run("Teste rápido: você está online?")
    print("Resposta do agente:", response)
except Exception as e:
    print("Erro ao acessar agente:", e)


