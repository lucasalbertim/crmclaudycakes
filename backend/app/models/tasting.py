from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import Base

class Tasting(Base):
    __tablename__ = "tastings"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    datetime = Column(DateTime, nullable=False)
    location = Column(String(255), nullable=True)
    status = Column(String(30), nullable=False, default="agendado")  # agendado, confirmado, realizado
    feedback = Column(Text, nullable=True)

    client = relationship("Client")
