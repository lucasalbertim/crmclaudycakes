from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import client
from app.routers import attachment
from app.routers import order
from app.routers import schedule
from app.routers import transaction
from app.routers import finance
from app.routers import installment
from app.routers import pipeline
from app.routers import supplier, purchase
from app.routers import project_cake
from app.routers import marketing
from app.routers import notification
from app.routers import dashboard
from app.routers import tasting
from app.routers import message_template, chatbot

app = FastAPI(title="Claudycakes CRM")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(client.router)
app.include_router(attachment.router)
app.include_router(order.router)
app.include_router(schedule.router)
app.include_router(transaction.router)
app.include_router(finance.router)
app.include_router(installment.router)
app.include_router(pipeline.router)
app.include_router(supplier.router)
app.include_router(purchase.router)
app.include_router(project_cake.router)
app.include_router(marketing.router)
app.include_router(notification.router)
app.include_router(dashboard.router)
app.include_router(tasting.router)
app.include_router(message_template.router)
app.include_router(chatbot.router)

@app.get("/")
def root():
    return {"message": "Bem-vindo ao CRM Claudycakes!"}
