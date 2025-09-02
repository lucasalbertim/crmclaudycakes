from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class OrderBase(BaseModel):
    contract_number: Optional[str] = None
    event_date: date
    status: Optional[str] = "planejamento"
    total_value: float
    description: Optional[str] = None
    notes: Optional[str] = None
    client_id: int
    pipeline_stage_id: Optional[int] = None

class OrderCreate(OrderBase):
    pass

class OrderRead(OrderBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
