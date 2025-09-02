from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.order import Order
from app.models.client import Client
from app.schemas.order import OrderCreate, OrderRead
from typing import List

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/", response_model=OrderRead)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == order.client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@router.get("/client/{client_id}", response_model=List[OrderRead])
def list_orders(client_id: int, db: Session = Depends(get_db)):
    return db.query(Order).filter(Order.client_id == client_id).all()
