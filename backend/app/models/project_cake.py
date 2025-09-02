from sqlalchemy import Column, Integer, String, Text, Date, Boolean
from app.core.database import Base

class ProjectCake(Base):
    __tablename__ = "project_cakes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    category = Column(String(50), nullable=False)  # casamento, aniversário, debutante, infantil
    photo = Column(String(255), nullable=True)
    date = Column(Date, nullable=True)
    is_reference = Column(Boolean, default=False)
