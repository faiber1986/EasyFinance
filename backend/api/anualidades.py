# backend/api/anualidades.py
from fastapi import APIRouter, HTTPException
from backend.schemas import FlujoRequest, FlujoResponse
from backend.core.cashflows import calcular_flujo

router = APIRouter(
    prefix="/api/math/flujos",
    tags=["Anualidades y Gradientes"]
)

@router.post("/", response_model=FlujoResponse)
def calcular_instrumentos(req: FlujoRequest):
    try:
        tasa_dec = req.tasa / 100.0
        # El gradiente geométrico es una tasa, debe ir en decimal. El aritmético es capital (moneda).
        grad_val = req.gradiente / 100.0 if "Geometrico" in req.tipo_instrumento else req.gradiente
        
        resultado = calcular_flujo(
            tipo_calculo=req.tipo_calculo,
            tipo_instrumento=req.tipo_instrumento,
            tasa=tasa_dec,
            n=req.periodos,
            A=req.cuota_base,
            gradiente=grad_val
        )
        
        return FlujoResponse(valor_calculado=resultado, mensaje="Cálculo exitoso")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error en el motor de flujos.")

