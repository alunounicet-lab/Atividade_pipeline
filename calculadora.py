def dividir(a: float, b: float) -> float:
    """Retorna a divisão de dois números, com tratamento de erro."""
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b