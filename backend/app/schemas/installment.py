from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class InstallmentBase(BaseModel):
    order_id: int
    transaction_id: Optional[int] = None
    due_date: date
    value: float
    status: Optional[str] = "em aberto"
    paid_date: Optional[datetime] = None

class InstallmentCreate(InstallmentBase):
    pass

class InstallmentRead(InstallmentBase):
    id: int

    class Config:
        orm_mode = True
