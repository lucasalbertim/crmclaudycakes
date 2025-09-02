from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.purchase import Purchase
from app.models.supplier import Supplier
from app.schemas.purchase import PurchaseCreate, PurchaseRead
from typing import List

router = APIRouter(prefix="/purchases", tags=["Purchases"])

@router.post("/", response_model=PurchaseRead)
def create_purchase(purchase: PurchaseCreate, db: Session = Depends(get_db)):
    supplier = db.query(Supplier).filter(Supplier.id == purchase.supplier_id).first()
    if not supplier:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    db_purchase = Purchase(**purchase.dict())
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase

@router.get("/supplier/{supplier_id}", response_model=List[PurchaseRead])
def list_purchases_by_supplier(supplier_id: int, db: Session = Depends(get_db)):
    return db.query(Purchase).filter(Purchase.supplier_id == supplier_id).all()

@router.get("/", response_model=List[PurchaseRead])
def list_purchases(db: Session = Depends(get_db)):
    return db.query(Purchase).all()

@router.patch("/{purchase_id}/pay", response_model=PurchaseRead)
def pay_purchase(purchase_id: int, db: Session = Depends(get_db)):
    purchase = db.query(Purchase).filter(Purchase.id == purchase_id).first()
    if not purchase:
        raise HTTPException(status_code=404, detail="Compra não encontrada")
    purchase.status = "pago"
    db.commit()
    db.refresh(purchase)
    return purchase
