from app.models.message_template import MessageTemplate
from sqlalchemy.orm import Session

def get_auto_response(db: Session, user_message: str) -> str:
    # Mini chatbot simples: busca por palavra-chave no nome ou categoria
    templates = db.query(MessageTemplate).all()
    for template in templates:
        if template.name.lower() in user_message.lower() or (
            template.category and template.category.lower() in user_message.lower()
        ):
            return template.content
    return "Desculpe, não entendi sua mensagem. Em breve retornaremos!"
