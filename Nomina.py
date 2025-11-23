""""
Crea un script en python que solicite los siguientes datos de los empleados
de una empresa:
Nombres Completos
Email
Numero movil
Genero MFO
Salario
Año de nacimiento

Despues de regisstrar un empleado, el sistema debe preguntar si desea agregar otro:
Validar que solo acepte S/s N/n; si ingresa un valor diferente, debe solicitar o requerir 
de nuevo la respuesta hasta que sea valida. 
La misma validacion para el genero MFO
Al finalizar de pedir empleados, debe presentar el siguiente reporte.

Cuatos empleados se registra
Total genero M
Total genero F
Total genero O
Total salarios a pagar 
Promedio de edades

Variables - condicionales - bucles y funciones
"""
total_empleados = 0
total_masculino = 0
total_femenino = 0
total_otro = 0
total_salarios = 0
acumulador_edades = 0
continuar = "S"

while continuar == "S" or continuar == "s":

    print("\nRegistro de Empleado")

    nombre = input("Nombres: ")
    email = input("Email: ")
    telefono = input("Numero de telefono: ")

    genero_valido = False
    while genero_valido == False:
        genero = input("Genero (Masculino/Femenino/Otro): ")

        if genero == "Masculino" or genero == "masculino":
            total_masculino += 1
            genero_valido = True
        elif genero == "Femenino" or genero == "femenino":
            total_femenino += 1
            genero_valido = True
        elif genero == "Otro" or genero == "otro":
            total_otro += 1
            genero_valido = True
        else:
            print("Error. Escoge tu genero: Masculino / Femenino / Otro")

    salario_valido = False
    while salario_valido == False:
        try:
            salario = float(input("Salario: "))
            salario_valido = True
        except:
            print("Ingrese un numero valido para salario.")

    año_valido = False
    while año_valido == False:
        try:
            año = int(input("Año de nacimiento: "))
            año_valido = True
            edad=2025-año
            acumulador_edades +=edad

        except:
            print("Error ingresa un año valido.")


    total_salarios += salario
    total_empleados += 1

    respuesta_valida = 0
    while respuesta_valida == False:
        continuar = input("Desea agregar otro empleado? (S/N): ")

        if continuar == "S" or continuar == "s" or continuar == "N" or continuar == "n":
            respuesta_valida = True
        else:
            print("Ingrese S o N.")



print("REPORTE FINAL")
print("Total empleados registrados:", total_empleados)
print("Total genero masculino:", total_masculino)
print("Total genero femenino:", total_femenino)
print("Total genero otro:", total_otro)
print("Total salarios a pagar:", total_salarios)


if total_empleados >0:
    promedio_edad=acumulador_edades/total_empleados
    print("Promedio de edad: ", round (promedio_edad,2), "años")
else:
    print("No hay empleados registrados")