salario = float(input("Digite o salário:"))

if (salario > 1250):
    print("Seu salário com aumento de 10%:R${:.2f}".format(salario+(salario*0.10)))
else:
    print("Seu salário com aumento de 15%:R${:.2f}".format(salario+(salario*0.15)))