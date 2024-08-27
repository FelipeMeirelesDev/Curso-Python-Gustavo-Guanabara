nota1 = float(input("Digite a primeira nota do aluno:"))
nota2 = float(input("Digite a segunda nota do aluno:"))

if ((nota1+nota2)/2) < 5:
    print("Reprovado")
elif ((nota1+nota2)/2) >= 5 and ((nota1+nota2)/2) <= 6.9:
    print("Recuperação")
else:
    print("Aprovado")

print("Teste")