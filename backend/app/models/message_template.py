from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class MessageTemplate(Base):
    __tablename__ = "message_templates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    content = Column(Text, nullable=False)
    category = Column(String(50), nullable=True)  # ex: lembrete, confirmação, follow-up
