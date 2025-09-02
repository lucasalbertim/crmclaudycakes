from sqlalchemy import Column, Integer, String
from app.core.database import Base

class PipelineStage(Base):
    __tablename__ = "pipeline_stages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique=True)
    order = Column(Integer, nullable=False)  # para ordenação visual
