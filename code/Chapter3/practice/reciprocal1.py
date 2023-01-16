n = int(input("Enter n: "))

sum = 0
for i in range(1, n + 1):
    sum += 1 / i

print("Sum = %.2f" % sum)