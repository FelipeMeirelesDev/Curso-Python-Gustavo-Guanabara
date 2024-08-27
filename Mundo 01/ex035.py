reta1 = float(input("Digite o tamanho da reta 01:"))
reta2 = float(input("Digite o tamanho da reta 02:"))
reta3 = float(input("Digite o tamanho da reta 03:"))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("Os segmentos acima podem formar um triângulo")
else:
    print("Os segmentos acima não podem formar um triângulo")