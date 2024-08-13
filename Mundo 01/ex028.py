import random

numero_aleatorio = random.randint(0, 5)

print("Jogo da advinhação:")
num = int(input("Digite o número que você acha que foi sorteado: "))

if num == numero_aleatorio:
    print("Você acertou!")
else:
    print("Você errou!")
    print("O número era:{}".format(numero_aleatorio))