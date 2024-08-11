#crie um programa que leio o nome de uma cidade e diga
#se ela começa ou não com o nome "SANTO".

cidade = str(input("Em que cidade você nasceu?:")).strip()

cidade.upper()

print(cidade[:5].upper() == "SANTO")

