from openclaw import OpenClaw
import sys

# Agora com o token prefixado com cmdop_
TOKEN = "cmdop_b8c89901621f30b808c6fa8fff2cf2ad460584abc9792374"
SERVER = "localhost:18789"

def test_connection():
    print(f"--- Teste Final de Conexão (SDK Python) ---")
    
    try:
        # 1. Instanciar o cliente via .remote()
        # O parâmetro 'insecure=True' é essencial para conexões locais (sem SSL)
        print(f"Conectando a {SERVER} (api_key format OK)...")
        
        client = OpenClaw.remote(
            api_key=TOKEN,
            server=SERVER,
            insecure=True
        )
        
        print("✓ Cliente autenticado com sucesso.")

        # 2. Solicitar resposta do agente
        print("Enviando comando para o agente...")
        # Nota: client.agent.run() é o comando padrão da SDK para enviar prompts
        response = client.agent.run("Responda apenas 'CONEXAO OK' se você estiver ouvindo.")
        
        print(f"✓ Resposta: {response}")
        print("--- CONEXÃO VALIDADA COM SUCESSO! ---")

    except Exception as e:
        print(f"✖ Erro: {type(e).__name__}: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    test_connection()
