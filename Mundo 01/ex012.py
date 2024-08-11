#Leia um preço de um produto e mostre o desconto de 5% nele
produto = int(input("Digite o valor do produto:"))
print("O seu novo preço com 5% de desconte é de R${:.2f}".format(produto-(produto*5/100)))