from Class.product_factory import ProductFactory
from Class.product import Product
from Class.supplier import Supplier

class Inventory:
    
    def __init__(self) -> None:
        self.__products = {}
        self.__product_factory = ProductFactory()

    def load_inventory(self, data: dict) -> None:
        for product_id, product_data in data.items():
            supplier_data = product_data["supplier"]
            supplier = Supplier(
                supplier_data["supplier_id"],
                supplier_data["name"],
                supplier_data["contact_email"]
            )
            product_type = product_data["type"]
            product_name = product_data["name"]
            product_price = product_data["price"]
            product_stock = product_data["stock"]
            product_size = product_data["size"]

            product = self.__product_factory.create(product_type, supplier, product_id, product_name, product_price, product_stock, product_size)
            self.__products[product_id] = product

    def to_dict(self) -> dict:
        inventory_dict = {}
        for product_id, product in self.__products.items():
            supplier = product.get_supplier()
            inventory_dict[product_id] = {
                "name": product.get_product_name(),
                "price": product.get_product_price(),
                "stock": product.get_product_stock(),
                "type": product.get_product_type(),
                "size": product.get_product_size(),
                "supplier": {
                    "supplier_id": supplier.get_supplier_id(),
                    "name": supplier.get_name(),
                    "contact_email": supplier.get_contact_email()
                }
            }
        return inventory_dict

    def add_product(self, product: Product) -> None:
        self.__products[product.get_product_id()] = product

    def remove_product(self, product_id: str) -> None:
        if product_id in self.__products:
            del self.__products[product_id]
        else:
            print("Product not found.")

    def update_stock(self, product_id: str, quantity: int) -> None:
        if product_id in self.__products:
            self.__products[product_id].update_stock(quantity)
        else:
            print("Product not found.")

    def search_product(self, product_id: str) -> Product | None:
        if product_id in self.__products:
            return self.__products[product_id]
        else:
            print("Product not found.")
            return None

    def display_inventory(self) -> None:
        if not self.__products:
            print("Inventory is empty.")
        else:
            for product in self.__products.values():
                print(
                    product.display_information() +
                    f"Fulfillment Info: {product.get_fulfillment_info()}\n" +
                    product.get_supplier().display_information() + "\n"
                )