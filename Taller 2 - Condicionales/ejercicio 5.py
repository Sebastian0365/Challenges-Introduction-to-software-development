tipo_identificacion=input("Ingrese el tipo de identificación (CC, PS, CE, CI): ")
nombres=input("Ingrese sus nombres: ")
apellidos=input("Ingrese sus apellidos: ")
genero=input("Ingrese su género (M para mujer, H para hombre): ")
año_nacimiento=int(input("Ingrese su año de nacimiento: "))
telefono=input("Ingrese su numero de telefono: ")
salario=float(input("Ingrese su salario: "))

print("\n--- Información Ingresada ---")
print("Tipo de identificación: ", tipo_identificacion)
print("Nombres: ", nombres)
print("Apellidos: ", apellidos)
print("Género: ", genero)
print("Año de nacimiento: ", año_nacimiento)
print("Número de teléfono: ", telefono)
print("Salario: ", salario)

if salario  <= 1200000:
    if genero == "M":
        aumento=salario*0.10
        salario_final=salario+aumento

    else:
        aumento=salario*0.88
        salario_final=salario+aumento
elif salario > 1200000 and salario < 2000000:
    aumento=salario*0.05
    salario_final=salario+aumento

else:
    if genero=="M":
        aumento=salario*0.03
        salario_final=salario+aumento
    else:
        aumento=salario*0.025
        salario_final=salario+aumento

print("RESULTADO")
print("Aumento: ", aumento)
print("Salario final:", salario_final)