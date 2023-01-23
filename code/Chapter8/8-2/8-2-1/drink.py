from product import Product

class Drink(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.__size = size

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size