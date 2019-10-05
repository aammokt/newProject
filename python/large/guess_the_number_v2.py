#  Added logics to give high-low hint to player
# 
sec_no = int(5)

print("I am thinking of a number between 1 and 10.")

while True:
    user_guess = int(input("What's the number? "))
    if user_guess == sec_no:
        print("Yes! You win!")
        break
    elif user_guess < sec_no:
        print(f'{user_guess} is too low.')
    elif user_guess > sec_no:
        print(f'{user_guess} is too high.')