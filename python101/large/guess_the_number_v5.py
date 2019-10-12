# Added logic to allow player to restart a game after a win
#
import random
sec_no = random.randint(1, 10)
chances = int(5)
print("I am thinking of a number between 1 and 10.")
print("You have 5 guesses left.")
while chances > 0:
    user_guess = int(input("What's the number? "))
    if user_guess > 10 or user_guess < 1:
        print("Please enter a number between 1 and 10.")
    elif user_guess == sec_no:
        print("Yes! You win!")
        playon = input("Do you want to play again (Y or N)? ").upper()
        if playon == "N":
            print("Bye!")
            break
        else: 
            chances = 5
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