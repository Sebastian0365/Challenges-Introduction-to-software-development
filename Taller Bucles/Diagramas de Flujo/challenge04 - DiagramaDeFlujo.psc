Proceso challenge04
    Definir dado1, dado2, contador Como Entero
    Definir par_de_6 Como Logico
	
    contador <- 0
    par_de_6 <- Falso
	
    Mientras par_de_6 = Falso Hacer
        dado1 <- Aleatorio(1,6)
        dado2 <- Aleatorio(1,6)
        contador <- contador + 1
		
        Escribir "Lanzamiento ", contador, ": ", dado1, " - ", dado2
		
        Si dado1 = 6 Y dado2 = 6 Entonces
            par_de_6 <- Verdadero
            Escribir "¡Ha salido un par de 6!"
        FinSi
    FinMientras
	
    Escribir "Número total de lanzamientos hasta obtener un par de 6: ", contador
FinProceso