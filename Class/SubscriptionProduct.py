from Class.Product import Product
from Class.Supplier import Supplier

class SubscriptionProduct(Product):

    def __init__(self, supplier: Supplier, product_id: str, name: str, price: float, stock: int, type: str, size: float):
        super().__init__(supplier, product_id, name, price, stock, type)
        self.__size = size

    def get_fulfillment_info(self):
        return f"Product is a subscription service."

    def display_information(self):
        return super().display_information()