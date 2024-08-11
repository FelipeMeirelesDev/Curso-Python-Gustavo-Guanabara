#Faça um programa que leia o nome completo de uma pessoa.
#Ex: Ana Maria de Souza
#primeiro = Ana
#Último = Souza

n = str(input("Digite seu nome completo:")).strip()
nome = n.split()
print("Muito prazer em te conhecer:")
print("seu primeiro nome é {}".format(nome[0]))
print("seu ultimo nome é {}".format(nome[len(nome)-1]))