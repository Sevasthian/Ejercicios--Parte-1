import os
while True:
    os.system("clear")
    numero = int(input("Ingrese el numero: "))
    operacion = numero%2
    if operacion == 0:
        print("Su numero es par")
        input("Oprima una tecla para continuar...")
    else:
        print("Su numero es impar")
        input("Oprima una tecla para continuar...")
    
    