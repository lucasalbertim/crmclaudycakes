from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.client import Client
from app.schemas.client import ClientCreate, ClientRead
from typing import List

router = APIRouter(prefix="/clients", tags=["Clients"])

@router.post("/", response_model=ClientRead)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    db_client = Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

@router.get("/", response_model=List[ClientRead])
def list_clients(db: Session = Depends(get_db)):
    return db.query(Client).all()
