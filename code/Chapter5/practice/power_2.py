def power_2(x):
    if x == 0:
        return 1
    return 2 * power_2(x - 1)

def main():
    x = int(input("Enter x: "))
    print(power_2(x))

if __name__ == "__main__":
    main()