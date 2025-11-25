import random

dado1=random.randint(1, 6)
dado2=random.randint(1, 6)

print("Dado 1:", dado1)
print("Dado 2:", dado2)

if dado1%2 ==0:
    print("El primer dado es par")
else:
    print("El primer dado es impar")

if dado2%2 ==0:
    print("El segundo dado es par")
else:
    print("El segundo dado es impar")

if dado1 == dado2:
    print("YOU WIN!")
else:
    print("GAME OVER")