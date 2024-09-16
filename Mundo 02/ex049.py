#Faça uma tabuada

num = int(input("Digite o número para ser gerador a tabuada:"))

for i in range (0,11):
    print("{} x {} = {}".format(num,i,(num*i)))