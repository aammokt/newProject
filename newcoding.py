# print("Hello world")

# name = "Carlos"
# age = 25

# print(f'Parameter: {name
# greeting = "f'Hello {name_of_user}, it is very nice to meet you and your friend {name_of_friend}'"
name_of_user = input("What is your name? ")
length_of_name = len(name_of_user)
friend = 1
while friend < 100:
    if length_of_name > 0:
        name_of_friend = input ("What is your friend's name? ")
        length_of_friend_name = len(name_of_friend)
        if length_of_friend_name > 0:
            greeting = f'Hello {name_of_user}, it is very nice to meet you and your friend {name_of_friend}'
            print(greeting)
        else:
            print("I'll ask later...")
            break
    else:
        print("I'll ask later...")
        break