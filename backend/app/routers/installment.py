from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.installment import Installment
from app.models.order import Order
from app.schemas.installment import InstallmentCreate, InstallmentRead
from typing import List
from datetime import datetime

router = APIRouter(prefix="/installments", tags=["Installments"])

@router.post("/", response_model=InstallmentRead)
def create_installment(installment: InstallmentCreate, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == installment.order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    db_installment = Installment(**installment.dict())
    db.add(db_installment)
    db.commit()
    db.refresh(db_installment)
    return db_installment

@router.get("/order/{order_id}", response_model=List[InstallmentRead])
def list_installments(order_id: int, db: Session = Depends(get_db)):
    return db.query(Installment).filter(Installment.order_id == order_id).all()

@router.patch("/{installment_id}/pay", response_model=InstallmentRead)
def pay_installment(installment_id: int, db: Session = Depends(get_db)):
    installment = db.query(Installment).filter(Installment.id == installment_id).first()
    if not installment:
        raise HTTPException(status_code=404, detail="Parcela não encontrada")
    installment.status = "pago"
    installment.paid_date = datetime.now()
    db.commit()
    db.refresh(installment)
    return installment
