numero1= int(input("Ingrese el primer numero: "))
numero2= int(input("Ingrese el segundo numero: "))

print("MENU")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Todas")

opcion= int(input("Elija una opcion: "))

if opcion == 1:
    resultado = numero1 + numero2
    print("La suma es: ",resultado)

elif opcion == 2:
    resultado = numero1 - numero2
    print("La resta es: ", resultado)   

elif opcion == 3:
    resultado = numero1 * numero2
    print("La multiplicacion es: ", resultado)

elif opcion == 4:
    resultado = numero1 / numero2
    print("La division es: ", resultado)

elif opcion == 5:
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    print("La suma es: ", suma)
    print("La resta es: ", resta)
    print("La multiplicacion es: ", multiplicacion)
    print("La division es: ", division)

else:
    print("Opcion no valida")

    
