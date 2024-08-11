#Faça um programa que leia um numero de 0 a 9999
#e mostre na tela cada um dos digitos separados.
#Ex:
#Digite um número: 1834
#Unidade:4 Dezena:3 Centena:8 milhar:1

num = int(input("Informe um número:"))

n = str(num)

print("Unidade:{} Dezena:{} Centena:{} Milhar:{}".format(n[3],n[2],n[1],n[0]))