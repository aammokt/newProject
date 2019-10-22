user_str = input("Please enter a sentence to encrypt: ")
input_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
output_str = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
output_list = list(output_str)
cipher_txt = []

while user_str != "":
        for i in user_str:
                if i == " ":
                        cipher_txt.append(i)
                else:
                        index = int(input_str.find(i))
                        cipher_txt.append(output_list[index])
        out_str = "".join(cipher_txt)
        print(out_str)
        cipher_txt.clear()
        user_str = input("Please enter another sentence to encrypt: ")
