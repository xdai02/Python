lst = [int(x) for x in input("Enter a list: ").split()]
n = len(lst)

j = 0
for i in range(n):
    if lst[i] != 0:
        lst[i], lst[j] = lst[j], lst[i]
        j += 1

for i in range(n):
    print(lst[i], end=' ')
print()