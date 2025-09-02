from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.finance_reports import get_monthly_report
from typing import Dict

router = APIRouter(prefix="/finance", tags=["Finance"])

@router.get("/monthly-report/{year}", response_model=Dict[int, Dict[str, float]])
def monthly_report(year: int, db: Session = Depends(get_db)):
    return get_monthly_report(db, year)
