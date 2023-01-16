lst = [int(x) for x in input("Enter a list: ").split()]
n = len(lst)

target = int(input("Target: "))

for i in range(n):
    for j in range(i + 1, n):
        if lst[i] + lst[j] == target:
            print("Index: %d, %d" % (i, j))