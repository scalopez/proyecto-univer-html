#Oscar alejandro lopez diaz 
#000032737
#Lenguajes de programacion
#24/05/2025
#Operador logico and (&&)

#Pide al usuario que ingrese Dos  numeros
a = int(input("Ingresa un número: "))
b = int(input("Ingresa otro número: "))
#Valida si los dos numeros son mayores a 0
if a > 0 and b > 0:
    #si es verdadero imprime que ambos son positivos
    print("Ambos son positivos")
    #De no cumplirse alguno de los dos se imprime "almenos uno no es positivo"
else:
    print("Al menos uno NO es positivo")