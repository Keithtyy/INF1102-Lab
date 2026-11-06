from Class.PhysicalProduct import PhysicalProduct
from Class.DigitalProduct import DigitalProduct
from Class.SubscriptionProduct import SubscriptionProduct

class Inventory:
    
    def __init__(self):
        self.__products = {}

    def load_inventory(self, data):
        for product_id, product_data in data.items():
            if product_data["type"] == "physical":
                product = PhysicalProduct(
                    product_id,
                    product_data["name"],
                    product_data["price"],
                    product_data["stock"],
                    product_data["type"],
                    product_data["size"]
                )
            elif product_data["type"] == "digital":
                product = DigitalProduct(
                    product_id,
                    product_data["name"],
                    product_data["price"],
                    product_data["stock"],
                    product_data["type"],
                    product_data["size"]
                )
            else:
                product = SubscriptionProduct(
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