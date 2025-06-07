#Oscar alejandro lopez diaz 
#000032737
#Lenguajes de programacion
#24/05/2025
#Operador logico OR

#Pide al usuario que ingrese Dos  numeros
a = int(input("Ingresa un número: "))
b = int(input("Ingresa otro número: "))

# Verifica si al menos uno de los dos números es par usando el operador OR
if a % 2 == 0 or b % 2 == 0:
    # Si al menos uno es par, muestra este mensaje
    print("Al menos uno es par")
else:
    # Si ninguno es par, muestra este mensaje
    print("Ninguno es par")