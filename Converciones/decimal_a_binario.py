#Oscar alejandro lopez diaz 
#000032737
#Lenguajes de programacion
#24/05/2025
# decimal a binario

# Pide al usuario que ingrese un número entero
numero = int(input("Introduce un número entero: "))

# Guarda el número original para mostrarlo al final
numero_ingresado = numero

# Si el número es cero, su binario es simplemente '0'
if numero == 0:
    binario = "0"
else:
    binario = ""
    # Convertir el número a binario usando divisiones sucesivas por 2
    while numero > 0:
        residuo = numero % 2              
        binario = str(residuo) + binario  
        numero = numero // 2              
# Mostrar el número original y su binario
print(f"El número {numero_ingresado} en binario es {binario}")