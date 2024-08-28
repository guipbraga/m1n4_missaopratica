from Calculadora import Calculadora

def main():
    while True:
        valorA = float(input("Digite o primeiro valor: "))
        valorB = float(input("Digite o segundo valor: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        calculadora = Calculadora(valorA, valorB, operacao)
        calculadora.mostrarResultado()
        continuar = input("Você deseja continuar executando o programa? Digite S para SIM e N para NÃO: ").strip().lower()
        if continuar == 'n':
            print("Encerrando o programa.")
            break
if __name__ == "__main__":
    main()
