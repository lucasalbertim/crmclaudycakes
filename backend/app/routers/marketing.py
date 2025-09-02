from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.marketing import get_inactive_clients, get_birthday_clients
from app.schemas.client import ClientRead
from typing import List

router = APIRouter(prefix="/marketing", tags=["Marketing"])

@router.get("/inactive-clients", response_model=List[ClientRead])
def inactive_clients(months: int = 6, db: Session = Depends(get_db)):
    return get_inactive_clients(db, months)

@router.get("/birthday-clients", response_model=List[ClientRead])
def birthday_clients(month: int = None, db: Session = Depends(get_db)):
    return get_birthday_clients(db, month)
