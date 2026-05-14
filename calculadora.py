def divisao(a, b):
    # Verifica se o divisor não é zero para evitar erro
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

print(divisao(6, 3)) # Resultado: 2.0