'#Faça um programa que leia um ângulo qualquer e mostre o valor do seno, cosseno e tangente'

import math

angulo = float(input("Digite o ângulo que você deseja:"))
seno = math.sin(math.radians(angulo))
print("O ângulo de {} tem o SENO de {:.2f}".format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print("O ângulo  de {} tem o Cosse de {:.2f}".format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print("O ângulo  de {} tem a Tangente de {:.2f}".format(angulo, tangente))