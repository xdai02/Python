c = input("Enter a character: ")
if c >= 'a' and c <= 'z':
    print("Lowercase")
elif c >= 'A' and c <= 'Z':
    print("Uppercase")
elif c >= '0' and c <= '9':
    print("Digit")
else:
    print("Special character")