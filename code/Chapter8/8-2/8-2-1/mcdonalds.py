from food import Food
from drink import Drink

def main():
    food = Food("Cheeseburger", 5.45, 302)
    drink = Drink("Coke", 3.7, "Large")

    print("Food: %s ($%.2f) %d Kcal" % (
        food.get_name(), food.get_price(), food.get_calories())
    )
    print("Drink: %s ($%.2f) %s" % (
        drink.get_name(), drink.get_price(), drink.get_size())
    )

if __name__ == "__main__":
    main()