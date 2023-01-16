def print_board(row, col):
    for i in range(row):
        for j in range(col - 1):
            print("   |", end='')
        print()
        if i < row - 1:
            print("---+---+---")

print_board(3, 3)