Algoritmo ejercicio5
	Escribir "Ingrese el tipo de identificación (CC, PS, CE, CI): "
	Leer tipo_identificacion
	Escribir "Ingrese sus nombres: "
	Leer nombres
	Escribir "Ingrese sus apellidos: "
	Leer apellidos
	Escribir "Ingrese su género (M para mujer, H para hombre): "
	Leer genero
	Escribir "Ingrese su año de nacimiento: "
	Leer año_nacimiento
	Escribir "Ingrese su numero de telefono: "
	Leer telefono
	Escribir "Ingrese su salario: "
	Leer salario
	
	Escribir ""
	Escribir "--- Información Ingresada ---"
	Escribir "Tipo de identificación: ", tipo_identificacion
	Escribir "Nombres: ", nombres
	Escribir "Apellidos: ", apellidos
	Escribir "Género: ", genero
	Escribir "Año de nacimiento: ", año_nacimiento
	Escribir "Número de teléfono: ", telefono
	Escribir "Salario: ", salario
	
	Si salario <= 1200000 Entonces
		Si genero = "M" Entonces
			aumento <- salario * 0.10
			salario_final <- salario + aumento
		SiNo
			aumento <- salario * 0.88
			salario_final <- salario + aumento
		FinSi
	SiNo
		Si salario > 1200000 Y salario < 2000000 Entonces
			aumento <- salario * 0.05
			salario_final <- salario + aumento
		SiNo
			Si genero = "M" Entonces
				aumento <- salario * 0.03
				salario_final <- salario + aumento
			SiNo
				aumento <- salario * 0.025
				salario_final <- salario + aumento
			FinSi
		FinSi
	FinSi
	
	Escribir "RESULTADO"
	Escribir "Aumento: ", aumento
	Escribir "Salario final: ", salario_final
FinAlgoritmo