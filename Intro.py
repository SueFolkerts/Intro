import random

theAnswer = random.randint(1,100)

tries = 0
userGuess = 0
while userGuess != theAnswer:
    userGuess = int(input("Guess my number between 1 and 100 "))
    tries +=1
    if userGuess < theAnswer:
        print("Too low!")
    elif userGuess > theAnswer:
        print("Too high")
    else:
        print("You got it in ", tries, " tries!!!")