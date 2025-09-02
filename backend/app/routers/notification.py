from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.email_sender import send_email
from app.services.whatsapp_sender import send_whatsapp
from app.models.client import Client
from typing import List

router = APIRouter(prefix="/notifications", tags=["Notifications"])

@router.post("/email")
def notify_email(client_id: int, subject: str, body: str, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    if not client.email:
        raise HTTPException(status_code=400, detail="Cliente sem e-mail cadastrado")
    success = send_email(client.email, subject, body)
    return {"success": success}

@router.post("/whatsapp")
def notify_whatsapp(client_id: int, message: str, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    if not client.phone:
        raise HTTPException(status_code=400, detail="Cliente sem telefone cadastrado")
    success = send_whatsapp(client.phone, message)
    return {"success": success}
