import random
import string

def password_generator(length):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))

def main():
    length = int(input("Enter length of password: "))
    print(password_generator(length))

if __name__ == "__main__":
    main()