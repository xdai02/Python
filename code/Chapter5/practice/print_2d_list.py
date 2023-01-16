def print_2d_list(lst, row, col):
    if len(lst) != row * col:
        return
    for i in range(row):
        for j in range(col):
            print(lst[i * col + j], end=' ')
        print()

def main():
    lst = [int(x) for x in input("Enter a list: ").split()]

    row = int(input("Enter row: "))
    col = int(input("Enter column: "))

    print_2d_list(lst, row, col)

if __name__ == "__main__":
    main()