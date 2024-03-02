def invertir_numero(numero):
    numero_invertido = str(numero)[::-1]
    numero_invertido = int(numero_invertido)
    return numero_invertido
while True:
    numero_original = input("Ingresa un número: ")
    if len(numero_original) == 3 and numero_original.isdigit():
        numero_original=int(numero_original)
        break
    else:
        print("el número ingresado no tiene tres digitos. Por favor, intentalo de nuevo")

numero_invertido = invertir_numero(numero_original)
print("Elnumero invertido es:", numero_invertido)