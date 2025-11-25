Algoritmo ejercicio4
	Escribir "Ingrese el primer numero: "
	Leer numero1
	Escribir "Ingrese el segundo numero: "
	Leer numero2
	
	Escribir "MENU"
	Escribir "1. Sumar"
	Escribir "2. Restar"
	Escribir "3. Multiplicar"
	Escribir "4. Dividir"
	Escribir "5. Todas"
	
	Escribir "Elija una opcion: "
	Leer opcion
	
	Si opcion = 1 Entonces
		resultado <- numero1 + numero2
		Escribir "La suma es: ", resultado
	SiNo
		Si opcion = 2 Entonces
			resultado <- numero1 - numero2
			Escribir "La resta es: ", resultado
		SiNo
			Si opcion = 3 Entonces
				resultado <- numero1 * numero2
				Escribir "La multiplicacion es: ", resultado
			SiNo
				Si opcion = 4 Entonces
					resultado <- numero1 / numero2
					Escribir "La division es: ", resultado
				SiNo
					Si opcion = 5 Entonces
						suma <- numero1 + numero2
						resta <- numero1 - numero2
						multiplicacion <- numero1 * numero2
						division <- numero1 / numero2
						Escribir "La suma es: ", suma
						Escribir "La resta es: ", resta
						Escribir "La multiplicacion es: ", multiplicacion
						Escribir "La division es: ", division
					SiNo
						Escribir "Opcion no valida"
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo