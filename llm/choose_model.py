import os

def get_model():
    provider = os.getenv("LLM_PROVIDER", "openai")

    models = {
        "openai": "gpt-4",
        "google": "google/gemini-3-flash-preview"
    }

    if provider not in models:
        raise ValueError("Provider inválido")

    return models[provider]