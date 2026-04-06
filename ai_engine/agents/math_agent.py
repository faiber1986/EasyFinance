# ai_engine/agents/math_agent.py
from backend.core.interest import convertir_tasa
from backend.core.amortization import generar_tabla

class MathAgent:
    def tool_convertir_tasa(self, tasa_origen: float, n: int, tipo_origen: str, tipo_destino: str) -> str:
        # Tu lógica de backend/core/interest.py aquí...
        from backend.core.interest import convertir_tasa
        try:
            # Validación de seguridad: si Gemini envía 20 en lugar de 0.20
            if tasa_origen > 1:
                tasa_origen = tasa_origen / 100
                
            res = convertir_tasa(tasa_origen, n, tipo_origen, tipo_destino)
            return f"Resultado: {res*100:.4f}%"
        except Exception as e:
            return f"Error: {str(e)}"

