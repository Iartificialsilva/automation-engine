from openclaw import OpenClaw
import sys

# Token corrigido
TOKEN = "cmdop_b8c89901621f30b808c6fa8fff2cf2ad460584abc9792374"
SERVER = "localhost:18789"

def check_agent_status():
    print(f"--- Diagnóstico do Agente ---")
    
    try:
        # Tenta conectar explicitamente ao agente principal ('main')
        # Em instalações locais, o agente padrão deve ser 'main'
        print(f"Conectando ao gateway {SERVER} buscando o agente 'main'...")
        
        client = OpenClaw.remote(
            api_key=TOKEN,
            server=SERVER,
            agent_id="main", # Especificando o agente principal
            insecure=True
        )
        
        # Tenta um comando simples que não exige processamento de IA (ping)
        print("Testando comando de status...")
        try:
            # Verifica se o transporte está conectado
            if hasattr(client, 'is_connected') and client.is_connected():
                print("✓ Conexão de transporte estabelecida.")
            
            # Tenta um comando de baixo nível para ver se o agente acorda
            response = client.agent.run("ping")
            print(f"✓ Resposta do agente: {response}")
            print("--- AGENTE ONLINE E OPERACIONAL ---")
            
        except Exception as inner_e:
            print(f"✖ Erro ao interagir com o agente: {type(inner_e).__name__}: {str(inner_e)}")
            
    except Exception as e:
        print(f"✖ Erro de conexão: {type(e).__name__}: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    check_agent_status()
