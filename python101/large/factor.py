x = 1
number = int(input("Please enter a number: "))
print(f'The factors of {number} are: ')

while x <= number:
    if number % x == 0:
        m = number / x
        print(int(m))
    x += 1