#Desenvolva um programa que leia seis números inteiros e mostre
#a soma apenas daqueles que forem pares. Se o valor digitado for 
#impar. desconsidere-o.

soma = 0
for i in range(0,6):
    num = int(input("Digite o {} valor: ".format(i+1)))
    if i%2 == 0:
        soma += num
print(soma)