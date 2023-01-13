NUM_PEOPLE = 5

total = 0

i = 1
while i <= NUM_PEOPLE:
    height = float(input("Enter person %d's height: " % i))
    total += height
    i += 1

average = total / NUM_PEOPLE
print("Average height: %.2f" % average)