num = int(input('Enter a number: '))

reverse = 0
while num > 0:
    reverse = reverse * 10 + num % 10
    num //= 10

print("Reverse:", reverse)