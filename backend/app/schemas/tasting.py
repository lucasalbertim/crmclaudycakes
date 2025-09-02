from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TastingBase(BaseModel):
    client_id: int
    datetime: datetime
    location: Optional[str] = None
    status: Optional[str] = "agendado"
    feedback: Optional[str] = None

class TastingCreate(TastingBase):
    pass

class TastingRead(TastingBase):
    id: int
    class Config:
        orm_mode = True
