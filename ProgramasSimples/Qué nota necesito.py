C1 = float(input("Ingrese nota certamen 1: "))
C2 = float(input("Ingrese nota certamen 2: "))
NL = float(input("Ingrese nota laboratorio: "))

operacion = int((((3*(60 - (-NL*-0.3)))/0.7)-(C1)-(C2)))
print(f'''Necesita una nota de {operacion} en el certamen 3''')