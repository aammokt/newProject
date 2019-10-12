# Added limit to number of guesses user can have
# 
import random
sec_no = random.randint(1, 10)
chances = int(5)
print("I am thinking of a number between 1 and 10.")

while chances > 0:
    user_guess = int(input("What's the number? "))
    if user_guess > 10 or user_guess < 1:
        print("Please enter a number between 1 and 10.")
    elif user_guess == sec_no:
        print("Yes! You win!")
        break
    elif user_guess < sec_no:
        print(f'{user_guess} is too low.')
        chances -= 1
    elif user_guess > sec_no:
        print(f'{user_guess} is too high.')
        chances -= 1

    if chances != 0:
        print(f'You have {chances} guesses left')
    else:
        print("You ran out of guesses!")

        