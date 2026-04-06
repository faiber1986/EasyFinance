# backend/core/amortization.py

def generar_tabla(monto: float, tasa: float, periodos: int, sistema: str) -> list:
    tabla = []
    saldo = monto

    # Periodo 0 (Desembolso)
    tabla.append({
        "periodo": 0, "saldo_inicial": 0.0, "cuota": 0.0,
        "interes": 0.0, "abono_capital": 0.0, "saldo_final": monto
    })

    if sistema == "Frances":
        # Fórmula: A = P * [ i(1+i)^n ] / [ (1+i)^n - 1 ]
        if tasa == 0:
            cuota = monto / periodos
        else:
            cuota = monto * (tasa * (1 + tasa)**periodos) / ((1 + tasa)**periodos - 1)
        
        for n in range(1, periodos + 1):
            interes = saldo * tasa
            abono_capital = cuota - interes
            saldo_final = saldo - abono_capital
            
            tabla.append({
                "periodo": n,
                "saldo_inicial": round(saldo, 2),
                "cuota": round(cuota, 2),
                "interes": round(interes, 2),
                "abono_capital": round(abono_capital, 2),
                "saldo_final": round(abs(saldo_final), 2) # abs() para evitar -0.0 por redondeo
            })
            saldo = saldo_final
            
    elif sistema == "Aleman":
        abono_capital = monto / periodos
        
        for n in range(1, periodos + 1):
            interes = saldo * tasa
            cuota = abono_capital + interes
            saldo_final = saldo - abono_capital
            
            tabla.append({
                "periodo": n,
                "saldo_inicial": round(saldo, 2),
                "cuota": round(cuota, 2),
                "interes": round(interes, 2),
                "abono_capital": round(abono_capital, 2),
                "saldo_final": round(abs(saldo_final), 2)
            })
            saldo = saldo_final
    else:
        raise ValueError("Sistema de amortización no soportado")

    return tabla

