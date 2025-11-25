import random

total_tiros=0
suma=0
total_pares=0
total_impares=0

seguir_jugando=True

while seguir_jugando==True:
    numero=random.randint(1,6)
    total_tiros=total_tiros+1

    print("Lanzamiento", total_tiros, ":", numero)

    suma=suma+numero

    if numero ==1:
        total_impares=total_impares+1
    
    if numero==2:
        total_pares=total_pares+1
    
    if numero==3:
        total_impares=total_impares+1
    
    if numero==4:
        total_pares=total_pares+1

    if numero==5:
        total_impares=total_impares+1

    if numero==6:
        total_pares=total_pares+1

    respuesta=input("¿Desea lanzar el dado de nuevo? (si/no): ")

    if respuesta=="si":
        seguir_jugando=True
    else:
        seguir_jugando=False

print("Resumen de la partida:")
print("Total de lanzamientos:", total_tiros)
print("Suma total de los números obtenidos:", suma)
print("Total de números pares obtenidos:", total_pares)
print("Total de números impares obtenidos:", total_impares)
