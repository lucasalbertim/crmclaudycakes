from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.transaction import Transaction
from app.models.order import Order
from app.schemas.transaction import TransactionCreate, TransactionRead
from typing import List

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/", response_model=TransactionRead)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    if transaction.order_id:
        order = db.query(Order).filter(Order.id == transaction.order_id).first()
        if not order:
            raise HTTPException(status_code=404, detail="Pedido não encontrado")
    db_transaction = Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@router.get("/", response_model=List[TransactionRead])
def list_transactions(db: Session = Depends(get_db)):
    return db.query(Transaction).all()

@router.get("/order/{order_id}", response_model=List[TransactionRead])
def list_transactions_by_order(order_id: int, db: Session = Depends(get_db)):
    return db.query(Transaction).filter(Transaction.order_id == order_id).all()
