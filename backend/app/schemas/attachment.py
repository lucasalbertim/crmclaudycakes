from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AttachmentBase(BaseModel):
    filename: str
    filepath: str
    type: Optional[str] = None

class AttachmentCreate(AttachmentBase):
    client_id: int

class AttachmentRead(AttachmentBase):
    id: int
    uploaded_at: datetime
    client_id: int

    class Config:
        orm_mode = True
