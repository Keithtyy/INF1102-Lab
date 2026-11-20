import os
import json
from Class.inventory import Inventory

class FileManager:

    def __init__(self, filename: str = "inventory.json") -> None:
        self.__filename = filename

    def load_inventory(self) -> dict:
        if not os.path.exists(self.__filename):
            with open(self.__filename, "w") as file:
                json.dump({}, file, indent=4)
                data = {}
        with open(self.__filename, "r") as file:
            data = json.load(file)
        return data

    def save_inventory(self, inventory: Inventory) -> None:
        with open(self.__filename, "w") as file:
            json.dump(inventory.to_dict(), file, indent=4)

    def load_csv_inventory(self, csv_filename: str) -> dict:
        try:
            file = open(csv_filename, "r")
        except FileNotFoundError:   
            raise FileNotFoundError(f"{csv_filename} does not exist.")
        data = {}
        with open(csv_filename, "r") as file:
            lines = file.readlines()
            for line in lines[1:]:  # Skip header
                product_id, name, price, stock, product_type, size, supplier_id, supplier_name, supplier_email = line.strip().split(",")
                data[product_id] = {
                    "name": name,
                    "price": float(price),
                    "stock": int(stock),
                    "type": product_type,
                    "size": float(size) if size else 0,
                    "supplier": {
                        "supplier_id": supplier_id,
                        "name": supplier_name,
                        "contact_email": supplier_email
                    }
                }
        return data