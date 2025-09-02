from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.attachment import Attachment
from app.schemas.attachment import AttachmentRead
from app.models.client import Client
import os
from typing import List

router = APIRouter(prefix="/attachments", tags=["Attachments"])
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/", response_model=AttachmentRead)
def upload_attachment(
    client_id: int = Form(...),
    type: str = Form(None),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    filepath = os.path.join(UPLOAD_DIR, file.filename)
    with open(filepath, "wb") as buffer:
        buffer.write(file.file.read())
    attachment = Attachment(
        client_id=client_id,
        filename=file.filename,
        filepath=filepath,
        type=type
    )
    db.add(attachment)
    db.commit()
    db.refresh(attachment)
    return attachment

@router.get("/client/{client_id}", response_model=List[AttachmentRead])
def list_attachments(client_id: int, db: Session = Depends(get_db)):
    return db.query(Attachment).filter(Attachment.client_id == client_id).all()
