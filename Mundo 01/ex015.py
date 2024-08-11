'''Faça um programa que pergunte a quantidade de km
percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. calcule o preço a pagar, sabendo que o carro
custa R$60 por dia e R$0.15 por km rodado.'''

kmpercorridos = float(input("Digite o quantidade de km percorridos:"))
diasalugado = int(input("Digite a quantidade dias que ele foi alugado:"))
valorapagar = (diasalugado*60)+(kmpercorridos*0.15)
print("O total a pagar vai ser de R${:.2f}".format(valorapagar))