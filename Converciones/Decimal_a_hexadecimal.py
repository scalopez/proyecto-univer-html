#Oscar alejandro lopez diaz 
#000032737
#Lenguajes de programacion
#24/05/2025
#decimal a hexadecimal
decimal = int(input("Ingresa un número decimal: "))

if decimal == 0:
    hexadecimal = "0"
else:
    hexadecimal = ""
    num = decimal
    while num > 0:
        residuo = num % 16
        if residuo < 10:
            caracter = str(residuo)
        else:
            caracter = chr(ord('A') + residuo - 10)
        hexadecimal = caracter + hexadecimal
        num //= 16

print("El número en hexadecimal es:", hexadecimal)