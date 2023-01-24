from out_of_stock_exception import OutOfStockException

class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def purchase(self):
        if self.stock <= 0:
            raise OutOfStockException(self.name + " is out of stock.")
        self.stock -= 1