print ("Number Guessing Game")

import random
n = random.randint(1,9)
print(n)
guess = int(input("Guess a number from 1 to 9:"))


if guess < n:
    print ("Guess was low")
    guess = int(input("Guess a number higher than that:"))

elif guess > n:
    print ("Guess was high")
    guess = int(input("Guess a number lower than that:"))

elif guess==n :
    print ("You guessed it !")

