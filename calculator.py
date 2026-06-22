opcao = 0
pi = 3.14
while opcao != 5:
    print("====================")
    print("Calculadora de Área")
    print("====================")

    print("1) Triangulo\n2) Retângulo\n3) Quadrado\n4) Circulo\n5) Sair\n")
    opcao = int(input("Qual forma: "))

    if opcao == 1:
        base = int(input("base: "))
        altura = int(input("altura: "))
        area = (altura * base) / 2
        print("A area é: ", area)
    elif opcao == 2:
        comprimento = int(input("Comprimento: "))
        largura = int(input("Largura: "))
        area = largura * comprimento
        print("A area é: ", area)
    elif opcao == 3:
        lado = int(input("Lado: "))
        area = lado ** 2
        print("A area é: ", area)
    elif opcao == 4:
        raio = int(input("Raio: "))
        area = pi * (raio**2)
        print("A area é: ", area)
    elif opcao == 5:
        print("Até mais!")
        break
    else:
        print("Opção inválida! Por favor tente novamente!")


