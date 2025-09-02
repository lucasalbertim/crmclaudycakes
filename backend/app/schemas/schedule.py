from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ScheduleBase(BaseModel):
    client_id: int
    order_id: Optional[int] = None
    delivery_datetime: datetime
    location: str
    status: Optional[str] = "planejamento"
    notes: Optional[str] = None
    project_photo: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None

class ScheduleCreate(ScheduleBase):
    pass

class ScheduleRead(ScheduleBase):
    id: int

    class Config:
        orm_mode = True
