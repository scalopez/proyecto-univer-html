#Oscar alejandro lopez diaz 
#000032737
#Lenguajes de programacion
#24/05/2025
# pirámide cuadrangular

# Base
b = float(input("Ingresa el valor de la base de tu pirámide: "))

# Altura
H = float(input("Ingresa el valor de la altura de tu pirámide: "))

# Área de la base
AB = b * b
print(f"El AB (Área de la base) es igual a: {AB}")

# Apotema lateral 
a = ((b / 2) ** 2 + H ** 2) ** 0.5
print(f"El apotema lateral es: {a}")

# Área lateral
al = 2 * b * a
print(f"El área lateral es: {al}")

# Volumen
v = (1 / 3) * AB * H
print(f"El volumen es: {v}")

# Área total
at = AB + al
print(f"El área total es: {at}")