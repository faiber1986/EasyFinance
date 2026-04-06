# backend/schemas.py
from pydantic import BaseModel, Field
from typing import List

class TasaRequest(BaseModel):
    tasa_origen: float = Field(..., description="Tasa en formato decimal (ej. 0.12 para 12%)")
    n: int = Field(..., gt=0, description="Número de periodos")
    tipo_origen: str
    tipo_destino: str

class TasaResponse(BaseModel):
    tasa_resultado: float
    mensaje: str

class AmortizacionRequest(BaseModel):
    monto: float = Field(..., gt=0, description="Monto del préstamo")
    tasa_interes: float = Field(..., description="Tasa periódica en porcentaje (ej. 1.5)")
    periodos: int = Field(..., gt=0, description="Plazo en meses/periodos")
    sistema: str = Field(..., description="'Frances' o 'Aleman'")

class FilaAmortizacion(BaseModel):
    periodo: int
    saldo_inicial: float
    cuota: float
    interes: float
    abono_capital: float
    saldo_final: float

class AmortizacionResponse(BaseModel):
    tabla: List[FilaAmortizacion]

class FlujoRequest(BaseModel):
    tipo_calculo: str = Field(..., description="'VP' (Valor Presente) o 'VF' (Valor Futuro)")
    tipo_instrumento: str = Field(..., description="'Anualidad Vencida', 'Anualidad Anticipada', 'Gradiente Aritmetico', 'Gradiente Geometrico'")
    tasa: float = Field(..., description="Tasa periódica en porcentaje")
    periodos: int = Field(..., gt=0)
    cuota_base: float = Field(..., description="Valor de la primera cuota (A)")
    gradiente: float = Field(0.0, description="Valor del gradiente (G en dinero, j en porcentaje)")

class FlujoResponse(BaseModel):
    valor_calculado: float
    mensaje: str

