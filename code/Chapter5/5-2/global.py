a, b = 1, 2

def swap():
    global a, b
    a, b = b, a
    print("swap(): a = %d, b = %d" % (a, b))

def main():
    print("Before: a = %d, b = %d" % (a, b))
    swap()
    print("After: a = %d, b = %d" % (a, b))

if __name__ == "__main__":
    main()