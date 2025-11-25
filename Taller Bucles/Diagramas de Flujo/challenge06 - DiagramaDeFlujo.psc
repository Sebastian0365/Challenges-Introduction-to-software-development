Proceso JuegoDeDadosInteractivo
    Definir numero, total_tiros, suma, total_pares, total_impares Como Entero
    Definir respuesta Como Cadena
    Definir seguir_jugando Como Logico
	
    total_tiros <- 0
    suma <- 0
    total_pares <- 0
    total_impares <- 0
    seguir_jugando <- Verdadero
	
    Mientras seguir_jugando = Verdadero Hacer
        numero <- Aleatorio(1,6)
        total_tiros <- total_tiros + 1
		
        Escribir "Lanzamiento ", total_tiros, ": ", numero
		
        suma <- suma + numero
		
        Si numero = 1 Entonces
            total_impares <- total_impares + 1
        FinSi
        Si numero = 2 Entonces
            total_pares <- total_pares + 1
        FinSi
        Si numero = 3 Entonces
            total_impares <- total_impares + 1
        FinSi
        Si numero = 4 Entonces
            total_pares <- total_pares + 1
        FinSi
        Si numero = 5 Entonces
            total_impares <- total_impares + 1
        FinSi
        Si numero = 6 Entonces
            total_pares <- total_pares + 1
        FinSi
		
        Escribir "¿Desea lanzar el dado de nuevo? (si/no): "
        Leer respuesta
		
        Si respuesta = "si" Entonces
            seguir_jugando <- Verdadero
        Sino
            seguir_jugando <- Falso
        FinSi
    FinMientras
	
    Escribir "Resumen de la partida:"
    Escribir "Total de lanzamientos: ", total_tiros
    Escribir "Suma total de los números obtenidos: ", suma
    Escribir "Total de números pares obtenidos: ", total_pares
    Escribir "Total de números impares obtenidos: ", total_impares
FinProceso
	
	
	
	
	
	
	
