def factorial(n):
    if n < 0:
        raise ValueError(
            "Factorial of negative numbers is not defined."
        )
    
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter n: "))
try:
    print(n, "! =", factorial(n))
except ValueError as e:
    print(e)