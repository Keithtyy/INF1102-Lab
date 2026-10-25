import json
import os

class Product:

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def get_product_name(self):
        return self.__name

    def get_product_price(self):
        return self.__price

    def get_product_stock(self):
        return self.__stock

    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self):
        return (
        f"Product ID: {self.__product_id}\n"
        f"Product Name: {self.__name}\n"
        f"Product Price: ${self.__price:.2f}\n"
        f"Product Stock: {self.__stock}\n"
        )

class Inventory:
    
    def __init__(self):
        self.__products = {}

    def load_inventory(self):
        if not os.path.exists("inventory.json"):
            with open("inventory.json", "w") as file:
                json.dump({}, file, indent=4)
                data = {}
        with open("inventory.json", "r") as file:
            data = json.load(file)
            print(data)
            for product_id, product_info in data.items():
                product = Product(
                    product_id,
                    product_info["name"],
                    product_info["price"],
                    product_info["stock"]
                )
                self.__products[product_id] = product
        return data

    def save_inventory(self):
        data = {}
        for product_id, product in self.__products.items():
            data[product_id] = {
                "name": product.get_product_name(),
                "price": product.get_product_price(),
                "stock": product.get_product_stock()
            }
        with open("inventory.json", "w") as file:
            json.dump(data, file, indent=4)

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

    def __init__(self,inventory):
        self.__inventory = inventory

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
                product_id = input("Product ID: ")
                product_name = input("Product Name: ")
                product_price = float(input("Product Price: "))
                product_stock = int(input("Product Stock: "))
                product = Product(product_id, product_name, product_price, product_stock)
                self.__inventory.add_product(product)
                print(f"Product added: {product_name}")
            except ValueError:
                print("Invalid price/stock quantity. Please enter only numeric values.")
        elif option == "3":
            product_id = input("Enter Product ID to update stock: ")
            new_stock = int(input("Enter new stock quantity: "))
            self.__inventory.update_stock(product_id, new_stock)
        elif option == "4":
            product_id = input("Enter Product ID to search: ")
            product = self.__inventory.search_product(product_id)
            if product:
                print(product.display_information())
        elif option == "5":
            self.__inventory.save_inventory()
            print("Inventory saved successfully.")
        elif option == "6":
            print("Exiting the program.")
            exit()
        else:
            print("Invalid option. Please try again.")

    
def main():
    inventory = Inventory()
    inventory.load_inventory()
    menu = Menu(inventory)

    while True:
        menu.display_menu()
        option = menu.get_user_input()
        menu.process_user_input(option)

main()