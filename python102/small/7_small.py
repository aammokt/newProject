numbers = [4,-2,55,6,-20,5,-11,8,0,-1]
multiplied_numbers =[]
factor = int(2)
print(numbers)
print(f'The factor for multiplication is {factor}')
for num in numbers:
    new_num = num * factor
    multiplied_numbers.append(new_num)

print(f'The following are the above list multiplied by the factor {factor}:')
print(multiplied_numbers)