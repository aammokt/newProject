user_entry = input("Please enter a string to translate: ")
entry = user_entry.upper()
leet_sentence = []

while True:
        if user_entry == "":
                break
        for letters in entry:
                if letters == "A":
                        leet_sentence.append(str(4))
                elif letters == "E":
                        leet_sentence.append(str(3))
                elif letters == "G":
                        leet_sentence.append(str(6))
                elif letters == "I":
                        leet_sentence.append(str(1))
                elif letters == "O":
                        leet_sentence.append(str(0))
                elif letters == "S":
                        leet_sentence.append(str(5))
                elif letters == "T":
                        leet_sentence.append(str(7))
                else:
                        leet_sentence.append(letters)
        new_sentence = "".join(leet_sentence)
        print("Translating to Leetspeak....")
        print(f'The Translation is: {new_sentence}')
        leet_sentence.clear()
        user_entry = input("Please enter a string to translate: ")
        entry = user_entry.upper()
