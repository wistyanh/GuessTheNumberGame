#guess the number game
from random import*
aRandomNumber = randint(1,20)
#To test and see chosen number: print(aRandomNumber)


while True:
    guess = input("Guess a number between 1 and 20: ")

    if guess == "stop":
        break

    if not guess.isnumeric():          #Makes sure input is a positive integer
        print("Positive integers only! Try again: ")
    else:
        guess = int(guess)

    if guess == aRandomNumber:
        print("Yes you got it! The number was " + str(aRandomNumber) + ".")
        break
    elif guess > aRandomNumber:
        print("Try again! Hint: It's a lower number. ")
    elif guess < aRandomNumber:
        print("Try again! Hint: It's a bigger number. ")
