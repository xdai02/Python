import math

n = int(input("Enter an integer: "))

is_prime = True
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")