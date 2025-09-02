from pydantic import BaseModel
from typing import Optional

class MessageTemplateBase(BaseModel):
    name: str
    content: str
    category: Optional[str] = None

class MessageTemplateCreate(MessageTemplateBase):
    pass

class MessageTemplateRead(MessageTemplateBase):
    id: int
    class Config:
        orm_mode = True
