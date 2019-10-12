coins = 0

while True:
    print(f'You have {coins} coins.')
    answer = input("Do you want another? ")
    coins += 1
    if answer == "no":
        print("Bye")
        break
