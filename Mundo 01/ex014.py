#Digite um temperatura em ºC e converta para ºF
temperaturac = float(input("Digite a temperátura em ºC:"))
f = 9 * temperaturac / 5 + 32
print("A conversão de {:.2f}ºC para ºf:{:.2f}ºf".format(temperaturac,f))