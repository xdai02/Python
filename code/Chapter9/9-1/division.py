while True:
    try:
        dividend = int(input("Enter an integer for dividend: "))
        divisor = int(input("Enter an integer for divisor: "))
        quotient = dividend / divisor
        print(dividend, "/", divisor, "=", quotient)
    except ValueError:
        print("Only integers supported.")
    except ZeroDivisionError:
        print("Divisor cannot be 0.")