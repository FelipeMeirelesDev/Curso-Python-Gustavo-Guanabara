casa = int(input("Digite o valor da casa:"))
salario = float(input("Digite o salario do comprador:"))
anos = int(input("Digite em quantos anos ele vai pagar:"))

prestacao = casa/(anos*12)

if prestacao > (salario*0.30):
    print("Empréstimo anulado")
else:
    print("Empréstimo aprovado")