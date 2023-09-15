"""I am writitng a program that allows users to guess number and if they guess a low number. the computer tell them to guess higher number."""

import random
number = random.randint(50,100)
guess = 0

while guess != number:

    guess = int(input("Enter guess number:"))
    if(guess < number):
     print("guess higher!")
    elif(guess > number):
     print("guess lower!")
    else:
     print("You won!")
