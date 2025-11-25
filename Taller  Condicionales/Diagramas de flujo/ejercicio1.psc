Algoritmo ejercicio1
	dado1 <- Aleatorio(1,6)
	dado2 <- Aleatorio(1,6)
	
	Escribir "Dado 1: ", dado1
	Escribir "Dado 2: ", dado2
	
	Si dado1 % 2 = 0 Entonces
		Escribir "El primer dado es par"
	SiNo
		Escribir "El primer dado es impar"
	FinSi
	
	Si dado2 % 2 = 0 Entonces
		Escribir "El segundo dado es par"
	SiNo
		Escribir "El segundo dado es impar"
	FinSi

	Si dado1 = dado2 Entonces
		Escribir "YOU WIN!"
	SiNo
		Escribir "GAME OVER"
	FinSi
FinAlgoritmo