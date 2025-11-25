Proceso ContarParesImpares
    Definir veces, numero, contador Como Entero
    Definir cantidad_pares, cantidad_impares Como Entero
	
    Escribir "¿Cuántas veces quieres lanzar el dado? "
    Leer veces
	
    cantidad_pares <- 0
    cantidad_impares <- 0
    contador <- 1
	
    Mientras contador <= veces Hacer
        numero <- Aleatorio(1,6)
        Escribir ""
        Escribir "Lanzamiento ", contador, ": ", numero
		
        Si numero = 1 Entonces
            cantidad_impares <- cantidad_impares + 1
        FinSi
        Si numero = 2 Entonces
            cantidad_pares <- cantidad_pares + 1
        FinSi
        Si numero = 3 Entonces
            cantidad_impares <- cantidad_impares + 1
        FinSi
        Si numero = 4 Entonces
            cantidad_pares <- cantidad_pares + 1
        FinSi
        Si numero = 5 Entonces
            cantidad_impares <- cantidad_impares + 1
        FinSi
        Si numero = 6 Entonces
            cantidad_pares <- cantidad_pares + 1
        FinSi
		
        contador <- contador + 1
		
        Escribir "Lanzamientos pares: ", cantidad_pares
        Escribir "Lanzamientos impares: ", cantidad_impares
    FinMientras
FinProceso
	
	
	
	
	
	
	
	
