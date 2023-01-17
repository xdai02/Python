from functools import reduce

lst = list(range(10))
print("lst =", lst)

odds = list(filter(lambda x: x % 2 == 1, lst))
print("odds =", odds)

squares = list(map(lambda x: x ** 2, odds))
print("squares =", squares)

sum = reduce(lambda x, y: x + y, squares)
print("sum =", sum)