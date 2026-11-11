from abc import ABC, abstractmethod
from Class.Supplier import Supplier


class Product(ABC):

    def __init__(self, supplier: Supplier, product_id: str, name: str, price: float, stock: int, type: str) -> None:
        self.__supplier = supplier
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__type = type

    @abstractmethod
    def get_fulfillment_info(self) -> str:
        pass

    def get_supplier(self) -> Supplier:
        return self.__supplier

    def get_product_id(self) -> str:
        return self.__product_id

    def get_product_name(self) -> str:
        return self.__name

    def get_product_price(self) -> float:
        return self.__price

    def get_product_stock(self) -> int:
        return self.__stock

    def get_product_type(self) -> str:
        return self.__type
    
    def update_stock(self, quantity: int) -> None:
        self.__stock = quantity

    def display_information(self) -> str:
        return (
        f"Product ID: {self.__product_id}\n"
        f"Product Name: {self.__name}\n"
        f"Product Price: ${self.__price:.2f}\n"
        f"Product Stock: {self.__stock}\n"
        f"Product Type: {self.__type}\n"
        )