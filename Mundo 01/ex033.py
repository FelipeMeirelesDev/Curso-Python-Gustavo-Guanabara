num1 = int(input("Digite o número 01:"))
num2 = int(input("Digite o número 02:"))
num3 = int(input("Digite o número 03:"))

if (num1 > num2 and num1 > num3):
    print("Número {} é maior".format(num1))
elif (num2 > num1 and num2 > num3):
    print("Número {} é maior".format(num2))
elif (num3 > num2 and num3 > num2):
    print("Número {} é maior".format(num3))