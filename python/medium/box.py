w = int(input("Enter Width: "))
h = int(input("Enter Height: "))
z = 1

while z <= h:
    if z == 1 or z == h:
        print("*"*w)
    else:
        print("*" + " "*(w - 2) + "*")
    z+= 1
