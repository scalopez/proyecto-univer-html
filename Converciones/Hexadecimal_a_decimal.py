#Oscar alejandro lopez diaz 
#000032737
#Lenguajes de programacion
#24/05/2025
#Hexadecimal a decimal

hexadecimal = input("Ingresa el número en hexadecimal: ")

decimal = 0
potencia = 0

# Recorrer la cadena de derecha a izquierda
for caracter in hexadecimal[::-1]:
    if caracter.isdigit():
        valor = int(caracter)
    else:
        valor = ord(caracter.upper()) - ord('A') + 10
    decimal += valor * (16 ** potencia)
    potencia += 1

print("El número decimal es:", decimal)