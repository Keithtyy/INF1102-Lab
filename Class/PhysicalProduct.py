from Class.Product import Product
from Class.CanBeShipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):

    def __init__(self, product_id, name, price, stock, type, size):
        super().__init__(product_id, name, price, stock, type, size)
        self.__size = size

    def get_fulfillment_info(self):
        return f"Product requires physical shipping."

    def calculate_shipping_cost(self):
        return self.__size * 5.0

    def display_information(self):
        return (
            super().display_information() +
            f"Product Size: {self.__size:.2f} kg\n"
        )