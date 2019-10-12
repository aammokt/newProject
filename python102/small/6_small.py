numbers = [4,-2,55,6,-20,5,-11,8,0,-1]
pos_numbers =[]
print(numbers)
for num in numbers:
    if num >= 0:
        pos_numbers.append(num)

print("The following are the list of positive numbers from the list above:")
print(pos_numbers)