import io
import core.config as config
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseUpload, MediaIoBaseDownload

def _initialize_drive_service():
    """
    Inicializa o serviço do Google Drive usando credenciais de Service Account.
    """
    try:
        credentials = service_account.Credentials.from_service_account_file(
            config.DRIVE_CREDENTIALS_PATH,
            scopes=['https://www.googleapis.com/auth/drive']
        )
        service = build("drive", "v3", credentials=credentials)
        return service
    except Exception as e:
        raise Exception(f"Erro ao inicializar serviço do Drive: {str(e)}")

def get_template(template_path: str) -> str:
    """
    Baixa o conteúdo de um template do Drive pelo ID (template_path).
    """
    service = _initialize_drive_service()
    try:
        request = service.files().get_media(fileId=template_path)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        
        return fh.getvalue().decode('utf-8')
    except HttpError:
        raise Exception("Erro ao buscar template no Drive")
    except Exception as e:
        raise Exception(f"Erro ao buscar template no Drive: {str(e)}")

def create_process_folder(numero_processo: str) -> str:
    """
    Cria uma pasta com o nome do número do processo dentro da pasta base configurada.
    """
    service = _initialize_drive_service()
    try:
        file_metadata = {
            'name': numero_processo,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [config.DRIVE_OUTPUT_BASE]
        }
        file = service.files().create(body=file_metadata, fields='id').execute()
        return file.get('id')
    except Exception:
        raise Exception("Erro ao criar pasta do processo")

def save_document(folder_path: str, file_name: str, content: str):
    """
    Salva o conteúdo gerado como um arquivo de texto (.txt) dentro da pasta do processo.
    """
    service = _initialize_drive_service()
    try:
        file_metadata = {
            'name': file_name,
            'parents': [folder_path]
        }
        media = MediaIoBaseUpload(
            io.BytesIO(content.encode('utf-8')),
            mimetype='text/plain',
            resumable=True
        )
        service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
    except Exception:
        raise Exception("Erro ao salvar documento no Drive")
