Proceso LanzarDadoVariasVeces
    Definir veces, suma, contador, numero Como Entero
	
    Escribir "¿Cuántas veces quieres lanzar el dado? "
    Leer veces
	
    suma <- 0
    contador <- 1
	
    Mientras contador <= veces Hacer
        numero <- Aleatorio(1,6)
        Escribir "Lanzamiento ", contador, ": ", numero
        suma <- suma + numero
        contador <- contador + 1
    FinMientras
	
    Escribir "La suma de todos los lanzamientos es: ", suma
FinProceso
