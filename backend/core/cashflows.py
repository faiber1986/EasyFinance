def calcular_flujo(tipo_calculo: str, tipo_instrumento: str, tasa: float, n: int, A: float, gradiente: float) -> float:
    i = tasa
    if i == 0:
        raise ValueError("La tasa de interés no puede ser cero.")
        
    vp = 0.0
    
    # 1. Cálculo del Valor Presente (VP)
    if tipo_instrumento == "Anualidad Vencida":
        vp = A * (1 - (1 + i)**-n) / i
        
    elif tipo_instrumento == "Anualidad Anticipada":
        vp = (A * (1 - (1 + i)**-n) / i) * (1 + i)
        
    elif tipo_instrumento == "Gradiente Aritmetico":
        G = gradiente
        vp_a = A * (1 - (1 + i)**-n) / i
        vp_g = (G / i) * (((1 - (1 + i)**-n) / i) - (n / (1 + i)**n))
        vp = vp_a + vp_g
        
    elif tipo_instrumento == "Gradiente Geometrico":
        j = gradiente # Viene en decimal si es tasa
        if i == j:
            vp = A * n / (1 + i)
        else:
            vp = A * (1 - ((1 + j)/(1 + i))**n) / (i - j)
    else:
        raise ValueError("Instrumento no soportado.")

    # 2. Retorno según el requerimiento
    if tipo_calculo == "VF":
        return vp * (1 + i)**n
    
    return vp