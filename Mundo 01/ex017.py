'#Faça um programa que leia o comprimento do cateto oposto e do adjacente e mostre a hipotenusa'

import math

catetooposto = float(input("Comprimento do cateto oposto"))
catetoadjacente = float(input("Comprimento do cateto adjacente"))
hipotenusa = math.hypot(catetooposto, catetoadjacente)
print("A Hipotenusa vai medir {:.2f}".format(hipotenusa))