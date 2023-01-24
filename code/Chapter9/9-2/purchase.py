from product import Product
from out_of_stock_exception import OutOfStockException

def main():
    product = Product("Cheeseburger", 50)

    try:
        for _ in range(60):
            product.purchase()
    except OutOfStockException as e:
        print(e)

if __name__ == "__main__":
    main()