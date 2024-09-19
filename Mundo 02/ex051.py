#desenvolva um programa que leia o primeiro termo e a razão
#de um PA. No final, mostre os 10 termos dessa progressão.

primeiro_termo = int(input("Primeiro Termo:"))
razao = int(input("Razão:"))

for i in range (0,10):
    print("{} ".format(primeiro_termo), end=" -> ")
    primeiro_termo += + razao
print("Acabou!")