from operacoes.adicao import somar
from operacoes.subtracao import subtrair
from operacoes.multiplicacao import multiplicar
from operacoes.divisao import dividir

def main():
    print("=== Calculadora Básica ===")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    try:
        opcao = int(input("Escolha a operação: "))
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        if opcao == 1:
            print(f"Resultado: {somar(a, b)}")
        elif opcao == 2:
            print(f"Resultado: {subtrair(a, b)}")
        elif opcao == 3:
            print(f"Resultado: {multiplicar(a, b)}")
        elif opcao == 4:
            print(f"Resultado: {dividir(a, b)}")
        else:
            print("Opção inválida.")

    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()