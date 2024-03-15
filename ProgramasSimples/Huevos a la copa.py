import math
rho = 1.038     
c = 3.7         
K = 5.4 * 10 ** (-3)  
Tw = 100
def huevoGrande():
        To = float(input("Escriba la temperatura original del huevo grande en grados Celsius: "))
        M = 67
        t = (M**(2/3) * c * rho**(1/3)) / (K * 3.1416**2) * (4 * 3.1416 / 3)**(2/3) * math.log(0.76 * (To - Tw) / (70 - Tw))

def huevoPequeño():
    To = float(input(f"Escriba la temperatura original del huevo pequeño en grados Celsius: "))
    M = 47
    t = (M**(2/3) * c * rho**(1/3)) / (K * 3.1416**2) * (4 * 3.1416 / 3)**(2/3) * math.log(0.76 * (To - Tw) / (70 - Tw))  
    print(f'''El tiempo necesario para preparar el huevo a la copa es de aproximadamente {t} segundos.''')
if(__name__ == "__main__"):
    print('''
    __  ___                                                   __           _         
   /  |/  /__  ____  __  __   ____  ____ __________ _   ___  / /__  ____ _(_)____    
  / /|_/ / _ \/ __ \/ / / /  / __ \/ __ `/ ___/ __ `/  / _ \/ / _ \/ __ `/ / ___/    
 / /  / /  __/ / / / /_/ /  / /_/ / /_/ / /  / /_/ /  /  __/ /  __/ /_/ / / /        
/_/  /_/\___/_/ /_/\__,_/  / .___/\__,_/_/   \__,_/   \___/_/\___/\__, /_/_/         
   __                     /_/ /\//              __        __     /____/              
  / /_____ _____ ___  ____ __//\/ ____     ____/ /__     / /_  __  _____ _   ______  
 / __/ __ `/ __ `__ \/ __ `/ __ \/ __ \   / __  / _ \   / __ \/ / / / _ \ | / / __ \ 
/ /_/ /_/ / / / / / / /_/ / / / / /_/ /  / /_/ /  __/  / / / / /_/ /  __/ |/ / /_/ / 
\__/\__,_/_/ /_/ /_/\__,_/_/ /_/\____/   \__,_/\___/  /_/ /_/\__,_/\___/|___/\____/  
                                                                                     

          1. Huevo grande
          2. Huevo pequeño
          3. Cerrar programa
          ''')
    opcion = int(input("Seleciones una opcion: "))
    if(opcion == 1):
         huevoGrande()
    elif(opcion == 2):
         huevoPequeño()
    elif(opcion == 3):
         exit()

    

