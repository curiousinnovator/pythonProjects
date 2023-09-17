"""import random

def guess(x):
    
    low = 1
    high = x
    feedback = " "
   
    while feedback != "c":
        if low != high:
            computer_guess = random.randint(low, high)
        else:
            computer_guess = low
            feedback = input(f'Is {computer_guess} too high(h), too low(L) or correct(C).')
        if feedback == "h": 
            high = computer_guess - 1
        elif feedback == "l":
            low = computer_guess + 1

    print("yesssss! the computer guessed your secret number correctly")

guess(100)"""


import random

def guess(x):
    low = 1
    high = x
    feedback = " "
   
    while feedback != "c":
        if low <= high:  # Check that the range is valid
            computer_guess = random.randint(low, high)
        else:
            print("You provided incorrect feedback. Please enter 'h', 'l', or 'c'.")
            break  # Exit the loop if invalid feedback is given

        feedback = input(f'Is {computer_guess} too high(h), too low(L) or correct(C): ').lower()
        
        if feedback == "h":
            high = computer_guess - 1
        elif feedback == "l":
            low = computer_guess + 1

    print("Yes! The computer guessed your secret number correctly")

guess(1000000)




