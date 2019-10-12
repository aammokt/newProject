list1 = [[1,3], [2,4]]
list2 = [[5,2], [1,0]]
new_list1 = []
new_list2 = []
result_list = []
x = len(list1)
y = len(list2)


for i in range(x):
    for j in range(y):
        if i == 0:
            num = list1[i][j] + list2[i][j]
            new_list1.append(num)
        else:
            num = list1[i][j] + list2[i][j]
            new_list2.append(num)
result_list.append(new_list1)
result_list.append(new_list2)

print(f'Result of matrix addition of {list1} and {list2} is {result_list}')