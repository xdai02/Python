from product import Product

class Food(Product):
    def __init__(self, name, price, calories):
        super().__init__(name, price)
        self.__calories = calories
    
    def get_calories(self):
        return self.__calories
    
    def set_calories(self, calories):
        self.__calories = calories
    
    def __str__(self):
        return "Food: %s %d Kcal" % (
            super().__str__(), self.__calories
        )