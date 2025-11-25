numero=int(input("Ingrese un numero entero: "))

print("El numero ingresado es ", numero)
      
if numero % 2 == 0:
    if numero > 0:
        print("El numero es PAR POSITIVO")
    else:
        print("El numero es PAR NEGATIVO")
else:
    if numero > 0:
        print("El numero es IMPAR POSITIVO")
    else:
        print("El numero es IMPAR NEGATIVO")

        
