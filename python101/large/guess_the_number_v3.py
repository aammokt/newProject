# Added randomizer to secret number
# Added logic to have user nput numbers between 1 to 10 only
import random
sec_no = random.randint(1, 10)

print("I am thinking of a number between 1 and 10.")

while True:
    user_guess = int(input("What's the number? "))
    if user_guess > 10 or user_guess < 1:
        print("Please enter a number between 1 and 10.")
    elif user_guess == sec_no:
        print("Yes! You win!")
        break
    elif user_guess < sec_no:
        print(f'{user_guess} is too low.')
    elif user_guess > sec_no:
        print(f'{user_guess} is too high.')
        