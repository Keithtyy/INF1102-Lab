import os
import json

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