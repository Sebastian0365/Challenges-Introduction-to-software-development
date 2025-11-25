import random

veces=int(input("Ingrese la cantidad de veces que desea lanzar el dado: "))

lado1=0
lado2=0
lado3=0
lado4=0
lado5=0
lado6=0

contador=1
while contador <= veces:
    lanzamiento=random.randint(1,6)
    print("Lanzamiento", contador, ":", lanzamiento)
    if lanzamiento == 1:
        lado1 += 1
    elif lanzamiento == 2:
        lado2 += 1
    elif lanzamiento == 3:
        lado3 += 1
    elif lanzamiento == 4:
        lado4 += 1
    elif lanzamiento == 5:
        lado5 += 1
    else:
        lado6 += 1
    contador += 1

contador=contador+1
print("Resultados de los lanzamientos:")
print(f"Lado 1: {lado1} veces")
print(f"Lado 2: {lado2} veces")
print(f"Lado 3: {lado3} veces")
print(f"Lado 4: {lado4} veces")
print(f"Lado 5: {lado5} veces")
print(f"Lado 6: {lado6} veces")


