'#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteado'

import random

nome1 = str(input("Digite o nome do aluno 01:"))
nome2 = str(input("Digite o nome do aluno 02:"))
nome3 = str(input("Digite o nome do aluno 03:"))
nome4 = str(input("Digite o nome do aluno 04:"))
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print("A ordem de apresentação será:")
print(lista)