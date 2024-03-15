numero = float(input("Ingrese un numero Real :"))
if numero >= 0:
    Decimal = numero % 1
    print(Decimal)
else:
    Decimal = -(numero % -1)
    print(Decimal)