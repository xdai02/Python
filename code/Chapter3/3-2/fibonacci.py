n = int(input("Enter the number of terms: "))

if n == 1:
    print(1)
elif n == 2:
    print(1, 1)
else:
    num1 = 1
    num2 = 1
    print(1, 1, end=' ')
    for i in range(3, n + 1):
        val = num1 + num2
        print(val, end=' ')
        num1 = num2
        num2 = val
    print()