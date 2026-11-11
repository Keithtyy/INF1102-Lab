from Class.Product import Product
from Class.Supplier import Supplier

class DigitalProduct(Product):

    def __init__(self, supplier: Supplier, product_id: str, name: str, price: float, stock: int, type: str, size: float):
        super().__init__(supplier, product_id, name, price, stock, type)
        self.__size = size

    def get_product_size(self):
        return self.__size

    def get_fulfillment_info(self):
        return f"Product is delivered digitally."

    def display_information(self):
        return (
            super().display_information() +
            f"Product Size: {self.__size:.2f} MB\n"
        )