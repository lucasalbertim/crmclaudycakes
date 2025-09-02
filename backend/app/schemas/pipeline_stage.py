from pydantic import BaseModel
from typing import Optional

class PipelineStageBase(BaseModel):
    name: str
    order: int

class PipelineStageCreate(PipelineStageBase):
    pass

class PipelineStageRead(PipelineStageBase):
    id: int
    class Config:
        orm_mode = True
