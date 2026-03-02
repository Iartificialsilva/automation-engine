import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env se existir
load_dotenv()

# --- CONFIGURAÇÕES DO GATEWAY (OpenClaw) ---
# Prioridade: Variável de ambiente -> Valor padrão
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")
OPENCLAW_API_KEY = os.getenv("OPENCLAW_API_KEY", "cmdop_b8c89901621f30b808c6fa8fff2cf2ad460584abc9792374")
OPENCLAW_SERVER = os.getenv("OPENCLAW_SERVER", "127.0.0.1:18789")

# --- CONFIGURAÇÕES DE IA / LLM ---
DEFAULT_MODEL = "google/gemini-3-flash"
ALLOWED_MODELS = {
    "simple": "google/gemini-3-flash",
    "complex": "google/gemini-3-pro"
}

# --- CONFIGURAÇÕES DO GOOGLE DRIVE ---
DRIVE_CREDENTIALS_PATH = os.getenv("DRIVE_CREDENTIALS_PATH", "credentials/google_drive.json")
DRIVE_OUTPUT_BASE = os.getenv("DRIVE_OUTPUT_BASE", "") # ID da pasta raiz no Drive

# --- REGRAS DE NEGÓCIO ---
MAX_RETRIES = 3
TEMPLATE_MAP = {
    "Contestação": "templates/contestacao_padrao.txt",
    "Petição de Pagamento": "templates/pagamento_voluntario.txt",
    "Especificação de Provas": "templates/provas_padrao.txt"
}
