from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.transaction import Transaction
from datetime import date
from typing import Dict

def get_monthly_report(db: Session, year: int) -> Dict:
    report = {}
    for month in range(1, 13):
        entries = db.query(func.sum(Transaction.value)).filter(
            Transaction.type == "entrada",
            func.extract('year', Transaction.date) == year,
            func.extract('month', Transaction.date) == month
        ).scalar() or 0
        exits = db.query(func.sum(Transaction.value)).filter(
            Transaction.type == "saída",
            func.extract('year', Transaction.date) == year,
            func.extract('month', Transaction.date) == month
        ).scalar() or 0
        report[month] = {
            "receita": entries,
            "despesa": exits,
            "saldo": entries - exits
        }
    return report
