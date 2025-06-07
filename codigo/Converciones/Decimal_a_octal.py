#Oscar alejandro lopez diaz 
#000032737
#Lenguajes de programacion
#24/05/2025
#Decimal a octal 
decimal = int(input("Ingresa un número decimal: "))

if decimal == 0:
    octal = "0"
else:
    octal = ""
    num = decimal
    while num > 0:
        residuo = num % 8
        octal = str(residuo) + octal
        num //= 8

print("El número en octal es:", octal)