class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price
    
    def __str__(self):
        return "%s ($%.2f)" % (self.__name, self.__price)