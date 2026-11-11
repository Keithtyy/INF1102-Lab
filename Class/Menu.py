from Class.PhysicalProduct import PhysicalProduct
from Class.DigitalProduct import DigitalProduct
from Class.SubscriptionProduct import SubscriptionProduct

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
        print("5. Remove Product")
        print("6. Save Inventory")
        print("7. Exit")
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
                    product_size = float(input("Product Weight: "))
                    product = PhysicalProduct(product_id, product_name, product_price, product_stock, product_type, product_size) 
                elif product_type == "digital":
                    product_size = float(input("Product Size: "))
                    product = DigitalProduct(product_id, product_name, product_price, product_stock, product_type, product_size)
                else:
                    product_size = "No size"
                    product = SubscriptionProduct(product_id, product_name, product_price, product_stock, product_type, product_size)
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
            try:
                product_id = input("Enter Product ID to remove: ")
                self.__inventory.remove_product(product_id)
            except ValueError:
                print("Invalid product ID. Please enter a valid product ID.")
        elif option == "6":
            self.__file_manager.save_inventory(self.__inventory)
            print("Inventory saved successfully.")
        elif option == "7":
            self.__file_manager.save_inventory(self.__inventory)
            print("Saving... before exiting.")
            print("Inventory saved successfully.")
            print("Exiting the program.")
            exit()
        else:
            print("Invalid option. Please try again.")