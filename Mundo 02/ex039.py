idade = int(input("Digite a idade do jovem:"))

if idade < 18:
    print("Ele ainda vai se alistar")
    print("Falta {} anos para o alistamento".format(18-idade))
elif idade == 18:
    print("Ele está na hora de de se alistar")
else:
    print("Já passou do tempo de alistamento!")
    print("Ele está com {} ano(s) de atraso!".format(idade-18))