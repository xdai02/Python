lst = [7, 4, 0, 3, 6, 8, 9, 2]

print("原始列表：", end='')
print(lst)

print("反转：", end='')
lst.reverse()
print(lst)

print("排序（升序）：", end='')
lst.sort()
print(lst)

print("排序（降序）：", end='')
lst.sort(reverse=True)
print(lst)