from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ai_engine.agents.financial_agent import FinancialAgent

router = APIRouter(prefix="/api/ia", tags=["Chatbot"])
agent_instance = FinancialAgent()

class ChatRequest(BaseModel):
    mensaje: str

@router.post("/consultar")
async def consultar_ia(req: ChatRequest):
    try:
        respuesta = agent_instance.chat(req.mensaje)
        return {"respuesta": respuesta}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

