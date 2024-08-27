from soma import somar
from subtracao import subtrair
from multiplicacao import multiplicar
from divisao import dividir
from resto_divisao import resto_divisao

historico = []

def mostrar_historico():
    if not historico:
        print("Histórico está vazio.")
    else:
        for item in historico:
            print(item)

while True:
    print("\nEscolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Resto da Divisão")
    print("6. Mostrar Histórico")
    print("7. Sair")

    escolha = input("Digite o número da operação: ")

    if escolha == '7':
        print("Saindo da calculadora. Até logo!")
        break
    elif escolha == '6':
        mostrar_historico()
    else:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            resultado = somar(num1, num2)
            operacao = f"{num1} + {num2} = {resultado}"
        elif escolha == '2':
            resultado = subtrair(num1, num2)
            operacao = f"{num1} - {num2} = {resultado}"
        elif escolha == '3':
            resultado = multiplicar(num1, num2)
            operacao = f"{num1} * {num2} = {resultado}"
        elif escolha == '4':
            resultado = dividir(num1, num2)
            operacao = f"{num1} / {num2} = {resultado}"
        elif escolha == '5':
            resultado = resto_divisao(num1, num2)
            operacao = f"{num1} % {num2} = {resultado}"
        else:
            print("Opção inválida, tente novamente.")
            continue

        print(operacao)
        historico.append(operacao)

