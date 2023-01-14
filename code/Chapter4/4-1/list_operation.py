lst = list(range(5))
print("lst =", lst)

lst.append(5)
print("append(5):", lst)

lst.insert(0, 8)
print("insert(0, 8):", lst)

lst.extend([8, 2, 3])
print("extend([8, 2, 3]):", lst)

lst.remove(5)
print("remove(5):", lst)

lst.pop(0)
print("pop(0):", lst)

print("index(3):", lst.index(3))

print("count(8):", lst.count(8))

lst.sort()
print("sort():", lst)

lst.sort(reverse=True)
print("sort(reverse=True):", lst)

lst.reverse()
print("reverse():", lst)

lst.clear()
print("clear():", lst)