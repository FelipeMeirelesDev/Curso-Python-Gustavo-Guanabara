ano_nascimento = int(input("Digite a idade do atleta:"))

idade = 2024 - ano_nascimento

if idade <= 9:
    print("Mirim")
elif idade > 9 and idade <= 14:
    print("Infantil")
elif idade > 14 and idade <= 19:
    print("Junior")
elif idade > 19 and idade <= 20:
    print("Senior")
else:
    print("Master")