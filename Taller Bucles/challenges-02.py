import random

veces=int(input("Cuantas veces quieres lanzar el dado? "))

suma=0
contador=1

while contador <= veces:
    numero=random.randint(1,6)
    print ("Lanzamiento", contador,  numero)
    suma=suma + numero
    contador=contador + 1

print("La suma de todos los lanzamientos es: ", suma)