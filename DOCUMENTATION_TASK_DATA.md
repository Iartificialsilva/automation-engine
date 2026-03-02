# Documentation: task_data Contract

The `task_data` dictionary must follow this structure to ensure consistency across the automation-engine, especially with the notifier and pipeline modules.

## Data Schema

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `numero_processo` | string | Yes | The legal process number. |
| `tipo_demanda` | string | No | The type of legal demand (e.g., Contestação, Petição). |
| `email_origem` | string | No | The sender's email address if originated from Gmail. |
| `texto_email` | string | Yes | The body text of the email or message content. |
| `anexos` | list | No | A list of attachments (file paths or metadata). |
| `origem` | string | Yes | The source of the task: "gmail" or "telegram". |
| `chat_id` | string | Conditional | Mandatory when `origem` is "telegram". |

---
*Note: This contract ensures that the `notifier.py` can correctly route status updates and final documents back to the original requester.*
