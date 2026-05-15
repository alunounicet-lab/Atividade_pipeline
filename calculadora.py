def dividir(a: float, b: float) -> float:
    
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b