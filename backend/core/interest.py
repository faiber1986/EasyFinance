# backend/core/interest.py
def convertir_tasa(tasa_origen: float, n: int, tipo_origen: str, tipo_destino: str) -> float:
    # 1. Llevar a EA
    ea = 0.0
    if tipo_origen == "Efectiva Anual (EA)":
        ea = tasa_origen
    elif tipo_origen == "Nominal":
        ea = (1 + tasa_origen / n)**n - 1
    elif tipo_origen == "Periódica":
        ea = (1 + tasa_origen)**n - 1
    else:
        raise ValueError("Tipo de tasa origen no soportado")

    # 2. Llevar al destino
    if tipo_destino == "Efectiva Anual (EA)":
        return ea
    elif tipo_destino == "Nominal":
        return n * ((1 + ea)**(1/n) - 1)
    elif tipo_destino == "Periódica":
        return (1 + ea)**(1/n) - 1
    else:
        raise ValueError("Tipo de tasa destino no soportado")

