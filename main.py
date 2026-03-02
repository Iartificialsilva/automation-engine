from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from core.controller import handle_new_task

app = FastAPI()

@app.post("/process-task")
async def process_task(request: Request):
    """
    Endpoint corporativo para processamento de tarefas jurídicas.
    Recebe o JSON, delega ao controller e retorna o resultado padronizado.
    """
    try:
        # a) Obter JSON
        try:
            task_data = await request.json()
        except Exception:
            return JSONResponse(
                status_code=400,
                content={"status": "error", "detail": "Corpo da requisição inválido"}
            )

        # b) Validar se o conteúdo é um dicionário
        if not isinstance(task_data, dict):
            return JSONResponse(
                status_code=400,
                content={"status": "error", "detail": "Formato inválido"}
            )

        # c) Chamar o controlador determinístico
        resultado = handle_new_task(task_data)

        # d) Retornar o resultado do controlador
        return JSONResponse(content=resultado)

    except Exception as e:
        # 5) Tratamento de erro inesperado no endpoint
        return JSONResponse(
            status_code=500,
            content={"status": "error", "detail": str(e)}
        )
