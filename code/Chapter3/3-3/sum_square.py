n = 10
print("Enter %d integers: " % n)

sum_square = 0
for i in range(n):
    num = int(input())
    if num < 0:
        continue
    sum_square += num * num

print("Sum of squares of positive integers:", sum_square)