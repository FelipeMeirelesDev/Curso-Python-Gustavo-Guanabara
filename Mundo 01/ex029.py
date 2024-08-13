velocidade_carro = int(input("Digite a velocidade de um carro:"))
limite = 80

if velocidade_carro > limite:
    print("Você foi multado!")
    print("A multa será no valor de R${}".format((velocidade_carro - limite)*7))
    