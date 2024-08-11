#crie um programa que leio o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas
#quantas letras ao todo(sem considerar espaçoes)
#quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome:")).strip()
print("Seu nome maiúsculo é {}".format(nome.upper()))
print("Seu nome minúsculo é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome)-nome.count(" ")))
print("Seu primeiro nome tem {} Letras".format(nome.find(" ")))