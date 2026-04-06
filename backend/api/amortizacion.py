from fastapi import APIRouter, HTTPException
from backend.schemas import AmortizacionRequest, AmortizacionResponse
from backend.core.amortization import generar_tabla

router = APIRouter(
    prefix="/api/math/amortizacion",
    tags=["Amortización"]
)

@router.post("/", response_model=AmortizacionResponse)
def calcular_amortizacion(req: AmortizacionRequest):
    try:
        tasa_decimal = req.tasa_interes / 100.0
        
        tabla_resultante = generar_tabla(
            monto=req.monto,
            tasa=tasa_decimal,
            periodos=req.periodos,
            sistema=req.sistema
        )
        return AmortizacionResponse(tabla=tabla_resultante)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

