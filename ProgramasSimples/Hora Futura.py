horaActual = int(input("Escriba la hora en que estas (ejem: son las 4:50 usted escribe que son las 4):"))
CantidadDeHoras = int(input("Escriba una cantidad de horas (ejm: 6, 7 ,9, 10...):  "))

if (horaActual >= 1) and (horaActual <= 12):
            operacion = horaActual + CantidadDeHoras
            if operacion <= 12:
                    print(operacion)
            else:
                    while operacion >= 12:
                        operacion -= 12 
                        print(f'''En {CantidadDeHoras} horas, el reloj marca las {operacion}''')
else:
        print("Error de hora")

            