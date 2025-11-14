Proceso LanzamientosDadoContador
    Definir veces, lanzamiento, contador Como Entero
    Definir lado1, lado2, lado3, lado4, lado5, lado6 Como Entero
	
    Escribir "Ingrese la cantidad de veces que desea lanzar el dado: "
    Leer veces
	
    lado1 <- 0
    lado2 <- 0
    lado3 <- 0
    lado4 <- 0
    lado5 <- 0
    lado6 <- 0
	
    contador <- 1
	
    Mientras contador <= veces Hacer
        lanzamiento <- Aleatorio(1,6)
        Escribir "Lanzamiento ", contador, ": ", lanzamiento
		
        Segun lanzamiento Hacer
            1:
                lado1 <- lado1 + 1
            2:
                lado2 <- lado2 + 1
            3:
                lado3 <- lado3 + 1
            4:
                lado4 <- lado4 + 1
            5:
                lado5 <- lado5 + 1
            6:
                lado6 <- lado6 + 1
        FinSegun
		
        contador <- contador + 1
    FinMientras
	
    Escribir "Resultados de los lanzamientos:"
    Escribir "Lado 1: ", lado1, " veces"
    Escribir "Lado 2: ", lado2, " veces"
    Escribir "Lado 3: ", lado3, " veces"
    Escribir "Lado 4: ", lado4, " veces"
    Escribir "Lado 5: ", lado5, " veces"
    Escribir "Lado 6: ", lado6, " veces"
FinProceso
