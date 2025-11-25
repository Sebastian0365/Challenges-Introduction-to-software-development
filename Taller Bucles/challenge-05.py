import random

veces=int(input("¿Cuántas veces quieres lanzar el dado? "))

cantidad_pares=0
cantidad_impares=0

contador=1

while contador<=veces:
    numero=random.randint(1,6)
    print("\n")

    print("Lanzamiento",contador,":",numero)

    if numero==1:
        cantidad_impares=cantidad_impares+1
    if numero==2:
        cantidad_pares=cantidad_pares+1
    if numero==3:
        cantidad_impares=cantidad_impares+1
    if numero==4:
        cantidad_pares=cantidad_pares+1
    if numero==5:
        cantidad_impares=cantidad_impares+1
    if numero==6:
        cantidad_pares=cantidad_pares+1

    contador=contador+1

    print("Lanzamientos pares:",cantidad_pares)
    print("Lanzamientos impares:",cantidad_impares)
