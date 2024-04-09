import random
import os

os.system('cls')

print("Välkommen till Gissa Talet. Spelet går ut på att du ska gisa ett tal mellan 1-100 under sju försök. Tryck 0 för att avsluta spelet.")

while True:
    number = random.randint(1, 100)
    tries = 0

    
    while tries < 7:
        try:
            guess = int(input("gissa "))
        except:
            print("Du skrev med bokstäver istället för siffror")
            continue
        

        if guess == number:
            break
   
        elif guess == 0:
            print("spelet är avslutat")
            exit()  
        
        elif guess < number:
            tries = tries + 1
            print("För lågt")
        elif guess > number:
            tries = tries + 1
            print("för högt")

    if tries == 7: 
        print("game over")
        print(f"Haha du hittade inte mitt hemliga tal. It was {number} Du får järna försöka igen. Tryck 0 för att avsluta")
        #exit()#

    else: 
        print(f"Du van och det tog, {tries+1} försök. Tryck 0 för att avsluta")