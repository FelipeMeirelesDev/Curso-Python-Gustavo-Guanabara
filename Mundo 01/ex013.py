#recebe um salário de um funcionário e mostre o aumento de 15%
salario=int(input("Digite o valor do salário do funcionário:R$"))
print("O novo salário com 15% de aumento é de:R${:.2f}".format(salario+(salario*15/100)))