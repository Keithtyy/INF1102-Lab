from Class.Product import Product
from Class.CanBeShipped import CanBeShipped
from Class.Supplier import Supplier

class PhysicalProduct(Product, CanBeShipped):

    def __init__(self, supplier: Supplier, product_id: str, name: str, price: float, stock: int, type: str, size: str):
        super().__init__(supplier, product_id, name, price, stock, type)
        self.__size = size

    def get_product_size(self):
        return self.__size

    def get_fulfillment_info(self):
        return f"Product requires physical shipping."

    def calculate_shipping_cost(self):
        return self.__size * 5.0

    def display_information(self):
        return (
            super().display_information() +
            f"Product Size: {self.__size:.2f} kg\n"
        )