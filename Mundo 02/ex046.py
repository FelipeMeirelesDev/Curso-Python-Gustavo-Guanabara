#Faça um programa que mostre na tela uma contagem refressiva para o
#estoura de fogos de artfício, indo de 10 até 0, com uma pausa de 1 segundos entre eles.

from time import sleep

for i in range(0,10):
    print(10-i)
    sleep(1)
print("Fogos estourando!")