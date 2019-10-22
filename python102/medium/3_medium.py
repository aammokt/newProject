SIZE = int(input("Please enter the size of the matrix to be added: "))
board1 = []
board2 = []
result_board = []

for y in range(SIZE):
        board1.append([])
        for x in range(SIZE):
                user_num = input(f'Please enter input for [{y}][{x}] on matrix 1: ')
                board1[y].append(user_num)

for row in board1:
        for column in row:
                print(f'{column}  ', end="")
        print("\n")

for y in range(SIZE):
        board2.append([])
        for x in range(SIZE):
                user_num = input(f'Please enter input for [{y}][{x}] on matrix 2: ')
                board2[y].append(user_num)

for row in board2:
        for column in row:
                print(f'{column}  ', end="")
        print("\n")

for y in range(SIZE):
        result_board.append([])
        for x in range(SIZE):
                new_sum = int(board1[x][y]) + int(board2[x][y])
                result_board[y].append(new_sum)

print("The result is sum between the two matrix are: \n")
for row in result_board:
        for column in row:
                print(f'{column}  ', end="")
        print("\n")
