user_str = input("Please enter a word with long vowels: ")

while user_str != "":
        if "aa" in user_str:
                index = user_str.find("aa")
                str_list = list(user_str)
                str_list.insert(index, "aaa")
                new_str = "".join(str_list)
                print(f'{user_str} => {new_str}')
                user_str = input("Please enter a word with long vowels: ")
        elif "ee" in user_str:
                index = user_str.find("ee")
                str_list = list(user_str)
                str_list.insert(index, "eee")
                new_str = "".join(str_list)
                print(f'{user_str} => {new_str}')
                user_str = input("Please enter a word with long vowels: ")
        elif "ii" in user_str:
                index = user_str.find("ii")
                str_list = list(user_str)
                str_list.insert(index, "iii")
                new_str = "".join(str_list)
                print(f'{user_str} => {new_str}')
                user_str = input("Please enter a word with long vowels: ")
        elif "oo" in user_str:
                index = user_str.find("oo")
                str_list = list(user_str)
                str_list.insert(index, "ooo")
                new_str = "".join(str_list)
                print(f'{user_str} => {new_str}')
                user_str = input("Please enter a word with long vowels: ")
        elif "uu" in user_str:
                index = user_str.find("uu")
                str_list = list(user_str)
                str_list.insert(index, "uuu")
                new_str = "".join(str_list)
                print(f'{user_str} => {new_str}')
                user_str = input("Please enter a word with long vowels: ")
        else:
                print(f'{user_str} => {user_str}')
                user_str = input("Please enter a word with long vowels: ")
