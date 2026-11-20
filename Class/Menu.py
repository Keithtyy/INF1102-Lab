from Class.supplier import Supplier
from Class.inventory import Inventory
from Class.file_manager import FileManager
from Class.product_factory import ProductFactory

class Menu:

    def __init__(self, inventory: Inventory, file_manager: FileManager) -> None:
        self.__inventory = inventory
        self.__product_factory = ProductFactory()
        self.__file_manager = file_manager

    def display_menu(self) -> None:
        print("-------MENU-------")
        print("1. Display Inventory")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Remove Product")
        print("6. Save Inventory")
        print("7. Exit")
        print("------------------")

    def get_user_input(self) -> str:
        user_input = input("Enter Option: ")
        return user_input

    def process_user_input(self, option: str) -> None:
        if option == "1":
            self.__inventory.display_inventory()
        elif option == "2":

            try:
                product_type = input("Enter Product Type (physical/digital/subscription): ").strip().lower()
                product_id = input("Product ID: ")
                product_name = input("Product Name: ")
                product_price = float(input("Product Price: "))
                product_stock = int(input("Product Stock: "))
                product_size = float(input("Product Size (weight in kg for physical, file size in MB for digital, or leave blank for subscription): ") or 0)

                supplier_id = input("Supplier ID: ")
                supplier_name = input("Supplier Name: ")
                supplier_email = input("Supplier Contact Email: ")
                supplier = Supplier(supplier_id, supplier_name, supplier_email)

                product = self.__product_factory.create(product_type, supplier, product_id, product_name, product_price, product_stock, product_size)
                self.__inventory.add_product(product)
                print(f"Product added: {product_name}")
            except ValueError as e:
                print(f"Invalid input: {e}")

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
                    print(product.display_information() + product.get_supplier().display_information())
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