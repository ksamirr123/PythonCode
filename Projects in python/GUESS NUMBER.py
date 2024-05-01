## GUESS THE NUMBER
import random

target = random.randint(1,9)

while True:
    userchoice =int(input("enter the user choice:"))
    if userchoice == target:
        print("correct guess.....")
        break
    elif userchoice<target:
        print("Guess the  Bigger Number ....TRY AGAIN")

    else:
        print("Guess the  Smaller Number ....TRY AGAIN")    


print("......GAME OVER......")        


