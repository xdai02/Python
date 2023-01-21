import random

NUM_FLIPS = 100

heads = 0

for _ in range(NUM_FLIPS):
    if random.randint(0, 1) == 0:
        heads += 1

print("Probability of heads:", heads / NUM_FLIPS)