from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.tasting import Tasting
from app.models.client import Client
from app.schemas.tasting import TastingCreate, TastingRead
from app.services.email_sender import send_email
from app.services.whatsapp_sender import send_whatsapp
from typing import List

router = APIRouter(prefix="/tastings", tags=["Tastings"])

@router.post("/", response_model=TastingRead)
def create_tasting(tasting: TastingCreate, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == tasting.client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    db_tasting = Tasting(**tasting.dict())
    db.add(db_tasting)
    db.commit()
    db.refresh(db_tasting)
    # Confirmação automática
    msg = f"Olá {client.name}, sua degustação está agendada para {db_tasting.datetime.strftime('%d/%m/%Y %H:%M')} no local: {db_tasting.location}."
    if client.email:
        send_email(client.email, "Confirmação de Degustação", msg)
    if client.phone:
        send_whatsapp(client.phone, msg)
    return db_tasting

@router.get("/client/{client_id}", response_model=List[TastingRead])
def list_tastings(client_id: int, db: Session = Depends(get_db)):
    return db.query(Tasting).filter(Tasting.client_id == client_id).all()

@router.patch("/{tasting_id}/feedback", response_model=TastingRead)
def add_feedback(tasting_id: int, feedback: str, db: Session = Depends(get_db)):
    tasting = db.query(Tasting).filter(Tasting.id == tasting_id).first()
    if not tasting:
        raise HTTPException(status_code=404, detail="Degustação não encontrada")
    tasting.feedback = feedback
    db.commit()
    db.refresh(tasting)
    return tasting
