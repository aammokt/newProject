list1 = [2, 4, 5]
list2 = [2, 3, 6]
new_list = []
i = 0
x = len(list1)

print(f'List 1 = {list1}')
print(f'List 2 = {list2}')

while i < x:
    num = list1[i] * list2[i]
    new_list.append(num)
    i +=1

print(f'{list1} * {list2} = {new_list}')