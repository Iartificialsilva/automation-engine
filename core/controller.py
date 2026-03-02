import core.config as config
import core.pipeline as pipeline
import core.validator as validator
import core.notifier as notifier
import core.logger as logger
import llm.classify as classify
import llm.choose_model as choose_model
import models.model_router as model_router
import integrations.drive_service as drive_service

def handle_new_task(task_data: dict) -> dict:
    """
    Controlador determinístico para processamento de novas tarefas jurídicas.
    Segue rigorosamente o fluxo de validação, classificação, geração e armazenamento.
    """
    try:
        # a) Validar presença obrigatória de campos
        required_fields = ["numero_processo", "texto_email", "origem"]
        for field in required_fields:
            if not task_data.get(field):
                raise ValueError(f"Campo obrigatório ausente: {field}")

        # b) Se tipo_demanda não estiver preenchido, classificar via LLM
        if not task_data.get("tipo_demanda"):
            task_data["tipo_demanda"] = classify.classify_demand(task_data["texto_email"])
        
        # c) Definir complexidade
        complexity = choose_model.get_complexity(task_data["texto_email"])
        
        # d) Converter complexidade para modelo real
        modelo_real = model_router.get_model(complexity)
        
        # e) Verificar se tipo_demanda existe no TEMPLATE_MAP
        tipo_demanda = task_data["tipo_demanda"]
        if tipo_demanda not in config.TEMPLATE_MAP:
            raise ValueError("Template não configurado para este tipo de demanda")
            
        # f) Buscar template no Drive
        template_path = config.TEMPLATE_MAP[tipo_demanda]
        template_content = drive_service.get_template(template_path)
        
        # g) Gerar e h/i) Validar com controle de retry
        texto_gerado = ""
        is_valid = False
        retry_count = 0
        
        while retry_count < config.MAX_RETRIES:
            # Geração
            texto_gerado = pipeline.generate_minuta(task_data, template_content, modelo_real)
            
            # Validação
            is_valid = validator.validate_all(texto_gerado, task_data)
            
            if is_valid:
                break
                
            retry_count += 1
            logger.log_info(f"Retry {retry_count} para o processo {task_data['numero_processo']}")

        # Verificação pós-loop de retry
        if not is_valid:
            notifier.notify_failure(task_data, "Falha na validação após retries")
            logger.log_error(f"Falha na validação após {config.MAX_RETRIES} retries para o processo {task_data['numero_processo']}")
            return {
                "status": "error",
                "detail": "Falha na validação após retries"
            }

        # j) Criar pasta do processo
        folder_path = drive_service.create_process_folder(task_data["numero_processo"])
        
        # k) Definir explicitamente o nome do arquivo
        file_name = f"DOC 01 - {tipo_demanda} - {task_data['numero_processo']}.docx"
        
        # l) Salvar documento
        drive_service.save_document(folder_path, file_name, texto_gerado)
        
        # m) Notificar sucesso
        notifier.notify_success(task_data, file_name)
        
        # n) Registrar finalização
        logger.log_info(f"Tarefa finalizada com sucesso: {file_name}")
        
        return {
            "status": "success", 
            "file_name": file_name
        }

    except Exception as e:
        # 5) Tratamento de erro inesperado
        logger.log_error(f"Erro inesperado no controller: {str(e)}")
        notifier.notify_failure(task_data, str(e))
        return {
            "status": "error",
            "detail": str(e)
        }
