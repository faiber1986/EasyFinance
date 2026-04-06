# backend/api/tasas.py
from fastapi import APIRouter, HTTPException
from ..schemas import TasaRequest, TasaResponse
from ..core.interest import convertir_tasa

router = APIRouter(
    prefix="/api/math/tasas",
    tags=["Tasas de Interés"]
)

@router.post("/", response_model=TasaResponse)
def calcular_tasas(req: TasaRequest):
    try:
        tasa_decimal = req.tasa_origen / 100.0
        
        resultado_decimal = convertir_tasa(
            tasa_origen=tasa_decimal,
            n=req.n,
            tipo_origen=req.tipo_origen,
            tipo_destino=req.tipo_destino
        )
        
        return TasaResponse(
            tasa_resultado=resultado_decimal * 100,
            mensaje="Cálculo exitoso"
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del motor de cálculo")

