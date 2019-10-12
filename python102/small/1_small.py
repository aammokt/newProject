numbers = [1,2,3,4,5]
x = len(numbers)
i = 0
total = 0

print(numbers)
while i < x:
    nums = int(numbers[i])
    total = total + nums
    i += 1

print(f'The sum of the list is {total}')