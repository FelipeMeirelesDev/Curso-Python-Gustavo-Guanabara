#Faça um programa que leia um número inteiro
#e diga se ele é primo ou se não é.

num = int(input("Digite um número: "))
cont = 0
for i in range(1,num + 1):
    if num % i == 0:
        print("\033[33m", end="")
        cont += 1
    else:
        print("\033[31m", end="")
    print("{} ".format(i), end="")
print("\nO número {} foi divisel {} vezes.".format(num,cont))