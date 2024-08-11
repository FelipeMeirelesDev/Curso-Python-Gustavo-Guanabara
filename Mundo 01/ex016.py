'#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.'

import math

num = float(input("Digite um número real:"))
print("O seu número inteiro é:",math.trunc(num))