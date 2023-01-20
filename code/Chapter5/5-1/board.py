def print_board():
    for i in range(3):
        for j in range(2):
            print("   |", end='')
        print()
        if i < 2:
            print("---+---+---")

print_board()