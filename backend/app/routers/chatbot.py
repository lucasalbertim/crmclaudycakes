from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.chatbot import get_auto_response

router = APIRouter(prefix="/chatbot", tags=["Chatbot"])

@router.post("/auto-response")
def auto_response(user_message: str, db: Session = Depends(get_db)):
    response = get_auto_response(db, user_message)
    return {"response": response}
