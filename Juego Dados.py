import os
from random import randint
lives=3
def roll_dice():
    dice1=randint(1-6)
    dice2=randint(1-6)
    return dice1, dice2
#print(roll_dice())
while True:
    key=input("Preciona una tecla para lanzar los dados: ")
    dices=roll_dice()
    print(f"dice1:{dices(0)}") 
    print(f"Dice2:{dices(1)}")
    if (dices[0]+dices[1])%2==0:
        lives+=1
    else:
        lives-=1
    if dices[0]and dices[1]==6:
        print ("Ganaste!")
    if lives ==0:
        print("Perdiste")
        break
    

