num = int(input("Enter an integer: "))
n = 0

while num != 0:
    num //= 10
    n += 1

print("Digits:", n)