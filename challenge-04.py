import random

contador=0

par_de_6=False

while par_de_6==False:
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    contador+=1
    print("Lanzamiento ",contador,": ",dado1," - ",dado2)
    
    if dado1==6:
        if dado2==6:
            par_de_6=True
            print("¡Ha salido un par de 6!")

print("Número total de lanzamientos hasta obtener un par de 6: ",contador)