SIZE = 3
board = []

for y in range(SIZE):
        board.append([])
        for x in range(SIZE):
                board[y].append("[%d][%d]" % (y,x))


for row in board:
        for column in row:
                print("%s " % column, end="")
        print("\n")

print("\n\nPlayer X is moving. \n\n")
board[0][2] = "X"
user_move_x = int(input("Please enter your move (x-coordinate): "))
user_move_y = int(input("Please enter your move (y-coordinate): "))
board[user_move_x][user_move_y] = "X"
for row in board:
        for column in row:
                print("%s " % column, end="")
        print("\n")
