
'''
crear un programa que pida los numeros y obtenga de resultado cual de ellos es par o si ambos lo son

'''


a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

if a % 2 == 0 and b % 2 == 0:
    print("Ambos números son pares.")
elif a % 2 == 0:
    print(f"El primer número {a} es par y el segundo número {b} es impar.")
elif b % 2 == 0:
    print(f"El segundo número {b} es par y el primer número {a} es impar.")
else:
    print("Ambos números son impares.")