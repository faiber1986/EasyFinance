# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api import tasas, amortizacion, anualidades, chatbot

app = FastAPI(title="Easy Finance API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar los módulos
app.include_router(tasas.router)
app.include_router(amortizacion.router)
app.include_router(anualidades.router)
app.include_router(chatbot.router)

@app.get("/")
def health_check():
    return {"status": "Easy Finance Backend Activo"}

