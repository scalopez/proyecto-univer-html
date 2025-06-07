#Oscar alejandro lopez diaz 
#000032737
#Lenguajes de programacion
#24/05/2025
#Binario a decimal
binario = input("Ingresa un número en binario: ")

decimal = 0
potencia = 0

# Recorrer la cadena de derecha a izquierda
for digito in binario[::-1]:
    decimal += int(digito) * (2 ** potencia)
    potencia += 1

print("El número decimal es:", decimal)