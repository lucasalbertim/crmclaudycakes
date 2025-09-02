from pydantic import BaseModel
from typing import Optional
from datetime import date

class PurchaseBase(BaseModel):
    supplier_id: int
    date: date
    item: str
    quantity: float
    unit_price: float
    total_price: float
    status: Optional[str] = "pendente"
    notes: Optional[str] = None

class PurchaseCreate(PurchaseBase):
    pass

class PurchaseRead(PurchaseBase):
    id: int
    class Config:
        orm_mode = True
