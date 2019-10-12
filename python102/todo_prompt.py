mylist = []
add_item = input("Please enter item into the list: ")
while add_item != "":
    mylist.append(add_item)
    print(mylist)
    add_item = input("Please enter item into the list: ")
    if add_item == "":
        print(mylist)
        break