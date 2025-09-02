from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.message_template import MessageTemplate
from app.schemas.message_template import MessageTemplateCreate, MessageTemplateRead
from typing import List

router = APIRouter(prefix="/message-templates", tags=["MessageTemplates"])

@router.post("/", response_model=MessageTemplateRead)
def create_template(template: MessageTemplateCreate, db: Session = Depends(get_db)):
    db_template = MessageTemplate(**template.dict())
    db.add(db_template)
    db.commit()
    db.refresh(db_template)
    return db_template

@router.get("/", response_model=List[MessageTemplateRead])
def list_templates(db: Session = Depends(get_db)):
    return db.query(MessageTemplate).all()

@router.patch("/{template_id}", response_model=MessageTemplateRead)
def update_template(template_id: int, template: MessageTemplateCreate, db: Session = Depends(get_db)):
    db_template = db.query(MessageTemplate).filter(MessageTemplate.id == template_id).first()
    if not db_template:
        raise HTTPException(status_code=404, detail="Modelo não encontrado")
    for key, value in template.dict().items():
        setattr(db_template, key, value)
    db.commit()
    db.refresh(db_template)
    return db_template
