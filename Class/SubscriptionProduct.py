from Class.Product import Product
from Class.Supplier import Supplier

class SubscriptionProduct(Product):

    def __init__(self, supplier: Supplier, product_id: str, name: str, price: float, stock: int, type: str, size: str) -> None:
        super().__init__(supplier, product_id, name, price, stock, type)
        self.__size = size

    def get_product_size(self) -> str:
        return self.__size

    def get_fulfillment_info(self) -> str:
        return f"Product is a subscription service."

    def display_information(self) -> str:
        return super().display_information()