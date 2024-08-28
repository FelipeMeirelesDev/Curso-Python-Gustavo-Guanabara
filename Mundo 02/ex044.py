produto = float(input("Digite o valor do produto:"))
print("Escolha a forma de pagamento:")
print("[1] A vista")
print("[2] 1x Cartão")
print("[3] 2x Cartão")
print("[4] 3x Cartão")
opcao = int(input())

if opcao == 1:
    print("O valor do produto a vista é de R${:.2f}".format(produto-(produto*0.10)))
elif opcao == 2:
    print("O valor do produto em 1x no cartão R${:.2f}".format(produto-(produto*0.05)))
elif opcao == 3:
    print("O valor do produto em 2x no cartão R${:.2f}".format(produto))
elif opcao == 4:
    print("O valor do produto em 3x no cartão R${:.2f}".format(produto+(produto*0.20)))
else:
    print("Opção Inválida")