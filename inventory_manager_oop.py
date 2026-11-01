import json
import os
from abc import ABC, abstractmethod

class Product(ABC):

    def __init__(self, product_id, name, price, stock, type):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__type = type

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
    
    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self):
        return (
        f"Product ID: {self.__product_id}\n"
        f"Product Name: {self.__name}\n"
        f"Product Price: ${self.__price:.2f}\n"
        f"Product Stock: {self.__stock}\n"
        )

class CanBeShipped(ABC):

    @abstractmethod
    def calculate_shipping_cost(self):
        pass


class PhysicalProduct(Product, CanBeShipped):

    def __init__(self, product_id, name, price, stock, type, weight):
        super().__init__(product_id, name, price, stock, type)
        self.__weight = weight

    def get_fulfillment_info(self):
        return f"Product requires physical shipping."

    def calculate_shipping_cost(self):
        return self.__weight * 5.0

    def get_product_weight(self):
        return self.__weight

    def display_information(self):
        return (
            super().display_information() +
            f"Product Weight: {self.__weight} kg\n"
        )

class DigitalProduct(Product):

    def __init__(self, product_id, name, price, stock, type, download_size):
        super().__init__(product_id, name, price, stock, type)
        self.__download_size = download_size

    def get_fulfillment_info(self):
        return f"Product is delivered digitally."

    def get_product_download_size(self):
        return self.__download_size

    def display_information(self):
        return (
            super().display_information() +
            f"Product Download Size: {self.__download_size:.2f} MB\n"
        )

class FileManager:

    def __init__(self, filename = "inventory.json"):
        self.__filename = filename

    def load_inventory(self):
        if not os.path.exists(self.__filename):
            with open(self.__filename, "w") as file:
                json.dump({}, file, indent=4)
                data = {}
        with open(self.__filename, "r") as file:
            data = json.load(file)
        return data

    def save_inventory(self, inventory):
        with open(self.__filename, "w") as file:
            json.dump(inventory.to_dict(), file, indent=4)

    

class Inventory:
    
    def __init__(self):
        self.__products = {}

    def load_inventory(self, data):
        for product_id, product_data in data.items():
            product = Product(
                product_id,
                product_data["name"],
                product_data["price"],
                product_data["stock"],
                product_data["type"],
                product_data["size"]
            )
            self.__products[product_id] = product

    def to_dict(self):
        inventory_dict = {}
        for product_id, product in self.__products.items():
            inventory_dict[product_id] = {
                "name": product.get_product_name(),
                "price": product.get_product_price(),
                "stock": product.get_product_stock(),
                "type": product.get_product_type(),
                "size": product.get_product_size()
            }
        return inventory_dict

    def add_product(self, product):
        self.__products[product.get_product_id()] = product

    def update_stock(self, product_id, quantity):
        if product_id in self.__products:
            self.__products[product_id].update_stock(quantity)
        else:
            print("Product not found.")

    def search_product(self, product_id):
        if product_id in self.__products:
            return self.__products[product_id]
        else:
            print("Product not found.")
            return None

    def display_inventory(self):
        if not self.__products:
            print("Inventory is empty.")
        else:
            for product in self.__products.values():
                print(product.display_information())

class Menu:

    def __init__(self,inventory, file_manager):
        self.__inventory = inventory
        self.__file_manager = file_manager

    def display_menu(self):
        print("-------MENU-------")
        print("1. Display Inventory")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("------------------")

    def get_user_input(self):
        user_input = input("Enter Option: ")
        return user_input

    def process_user_input(self, option):
        if option == "1":
            self.__inventory.display_inventory()
        elif option == "2":

            try:
                product_type = input("Enter Product Type (physical/digital): ").strip().lower()
                product_id = input("Product ID: ")
                product_name = input("Product Name: ")
                product_price = float(input("Product Price: "))
                product_stock = int(input("Product Stock: "))
                if product_type == "physical":
                    product_weight = float(input("Product Weight: "))
                    product = PhysicalProduct(product_id, product_name, product_price, product_stock, product_type, product_weight) 
                else:
                    product_size = float(input("Product Size: "))
                    product = DigitalProduct(product_id, product_name, product_price, product_stock, product_type, product_size)
                self.__inventory.add_product(product)
                print(f"Product added: {product_name}")
            except ValueError:
                print("Invalid price/stock quantity. Please enter only numeric values.")
        elif option == "3":
            try:
                product_id = input("Enter Product ID to update stock: ")
                new_stock = int(input("Enter new stock quantity: "))
                self.__inventory.update_stock(product_id, new_stock)
            except ValueError:
                print("Invalid stock quantity. Please enter only numeric values.")
        elif option == "4":
            try:
                product_id = input("Enter Product ID to search: ")
                product = self.__inventory.search_product(product_id)
                if product:
                    print(product.display_information())
            except ValueError:
                print("Invalid product ID. Please enter a valid product ID.")
        elif option == "5":
            self.__file_manager.save_inventory(self.__inventory)
            print("Inventory saved successfully.")
        elif option == "6":
            print("Exiting the program.")
            exit()
        else:
            print("Invalid option. Please try again.")

    
def main():
    file_manager = FileManager()
    data = file_manager.load_inventory()
    inventory = Inventory()
    inventory.load_inventory(data)
    menu = Menu(inventory, file_manager)

    while True:
        menu.display_menu()
        option = menu.get_user_input()
        menu.process_user_input(option)

main()
