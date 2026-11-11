
from Class.Product import Product

class OrderLine:

    def __init__(self, product: Product, quantity: int) -> None:
        self.__product = product
        self.__quantity = quantity

    def get_product(self) -> Product:
        return self.__product

    def get_quantity(self) -> int:
        return self.__quantity

    def calculate_subtotal(self) -> float:
        return self.__product.get_product_price() * self.__quantity

    def display_information(self) -> str:
        return (
            f"Product: {self.__product.get_product_name()} (ID: {self.__product.get_product_id()}) | "
            f"Unit Price: ${self.__product.get_product_price():.2f} | "
            f"Qty: {self.__quantity} | "
            f"Subtotal: ${self.calculate_subtotal():.2f}"
        )