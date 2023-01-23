from food import Food
from drink import Drink

def main():
    food = Food("Cheeseburger", 5.45, 302)
    drink = Drink("Coke", 3.7, "Large")

    print(food)
    print(drink)

if __name__ == "__main__":
    main()