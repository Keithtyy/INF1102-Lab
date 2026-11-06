from abc import ABC, abstractmethod


class Product(ABC):

    def __init__(self, product_id, name, price, stock, type, size):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__type = type
        self.__size = size

    @abstractmethod
    def get_fulfillment_info(self):
        pass

    def get_product_id(self):
        return self.__product_id

    def get_product_name(self):
        return self.__name

    def get_product_price(self):
        return self.__price

    def get_product_stock(self):
        return self.__stock

    def get_product_type(self):
        return self.__type

    def get_product_size(self):
        return self.__size
    
    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self):
        return (
        f"Product ID: {self.__product_id}\n"
        f"Product Name: {self.__name}\n"
        f"Product Price: ${self.__price:.2f}\n"
        f"Product Stock: {self.__stock}\n"
        f"Product Type: {self.__type}\n"
        f"Product Size: {self.__size}\n"
        )