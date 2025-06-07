#Oscar alejandro lopez diaz 
#000032737
#Lenguajes de programacion
#24/05/2025
#Octal a decimal
octal = input("Ingresa un número en octal: ")

decimal = 0
potencia = 0

# Recorrer la cadena de derecha a izquierda
for digito in octal[::-1]:
    decimal += int(digito) * (8 ** potencia)
    potencia += 1

print("El número decimal es:", decimal)