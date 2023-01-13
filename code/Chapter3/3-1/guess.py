import random

answer = random.randint(1, 100)
cnt = 0

while True:
    num = int(input("Guess a number: "))
    cnt += 1

    if num > answer:
        print("Too high")
    elif num < answer:
        print("Too low")
    else:
        break

print("Correct! You guessed %d times." % cnt)