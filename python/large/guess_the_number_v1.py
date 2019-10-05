sec_no = int(5)

print("I am thinking of a number between 1 and 10.")

while True:
    user_guess = int(input("What's the number? "))
    if user_guess == sec_no:
        print("Yes! You win!")
        break
    else:
        print("Nope, try again.")