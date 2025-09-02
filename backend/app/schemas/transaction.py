from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class TransactionBase(BaseModel):
    order_id: Optional[int] = None
    type: str  # entrada ou saída
    category: str  # receita, custo operacional, custo produção
    description: Optional[str] = None
    value: float
    date: date

class TransactionCreate(TransactionBase):
    pass

class TransactionRead(TransactionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
