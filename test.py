greeting = 'Hello %s, it is very nice to meet you and your friend %s'
name_of_user = input("Whats your name? ")
length_of_name = len(name_of_user)
if length_of_name > 0:
    name_of_friend = input ("What is your friend's name? ")
    print(greeting % (name_of_user, name_of_friend))
else:
    print("I'll ask later")