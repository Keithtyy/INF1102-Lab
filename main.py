from Class.FileManager import FileManager
from Class.Inventory import Inventory
from Class.Menu import Menu
    
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
