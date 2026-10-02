import json
import os

def load_inventory():
    if not os.path.exists("inventory.json"):
        with open("inventory.json", "w") as file:
            json.dump({}, file, indent=4)
            data = {}
    with open("inventory.json", "r") as file:
        data = json.load(file)
    return data
    
def save_inventory():
    with open("inventory.json", "w") as file:
        json.dump({}, file, indent=4)

def menu_input():
    print("-------MENU-------")
    print("1. Display Inventory")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("------------------")

    user_input = input("Enter Option: ")
    return user_input

def display_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        for product_id, product_info in inventory.items():
            print(f"ID: {product_id} | Name: {product_info['name']} | Price: {product_info['price']} | Stock: {product_info['stock']}")

def add_product(inventory):
    product_id =  str(input("Product ID: "))
    if product_id in inventory:
        print("Product already exists.")
        return inventory
    product_name = input("Product Name: ")
    product_price = input("Product Price: ") 
    product_stock = input("Product Stock: ")
    if not product_price.replace('.', '', 1).isdigit() or float(product_price) < 0:
        print("Invalid price. Please enter a valid numeric value.")
        return inventory
    if not product_stock.isnumeric() or int(product_stock) < 0:
        print("Invalid stock quantity. Please enter a valid numeric value.")
        return inventory
    inventory[product_id] = {
        "name": product_name,
        "price": float(product_price),
        "stock": int(product_stock)
    }
    print(f"Product added: {product_name}")
    return inventory

def update_stock(inventory):
    product_id = input("Enter Product ID to update stock: ")
    if product_id not in inventory:
        print("Product not found.")
        return inventory
    else:
        print(f"Current stock for product ID {product_id}: {inventory[product_id]['stock']}")
    new_stock = input("Enter new stock quantity: ")
    if not new_stock.isnumeric() or int(new_stock) < 0:
        print("Invalid stock quantity. Please enter a valid numeric value.")
        return inventory
    inventory[product_id]["stock"] = int(new_stock)
    print(f"Stock updated for product ID {product_id}.")
    return inventory

def search_product(inventory):
    product_id = input("Enter Product ID to search: ")
    if product_id not in inventory:
        print("Product not found.")
        return inventory
    else:
        product_info = inventory[product_id]
        print("Product Found:")
        print("-----------------")
        print(f"ID: {product_id}")
        print(f"Name: {product_info['name']}")
        print(f"Price: {product_info['price']}")
        print(f"Stock: {product_info['stock']}") 
        print("-----------------")

def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)
    print("Inventory saved successfully.")   

def exit_program():
    print("Saving inventory before exiting")
    save_inventory(inventory)
    print("Thank you for using the inventory management system.")
    print("Program terminated.")
    exit()

def user_input_handling(inventory):
    while True:
        menu_option = menu_input()
        if menu_option == "1":
            display_inventory(inventory)
        elif menu_option == "2":
            inventory = add_product(inventory)
        elif menu_option == "3":
            inventory = update_stock(inventory)
        elif menu_option == "4":
            search_product(inventory)
        elif menu_option == "5":
            save_inventory(inventory)
        elif menu_option == "6":
            exit_program()
        else:
            print("Invalid option. Please try again.")

inventory = load_inventory()
user_input_handling(inventory)

#Link to github repo: https://github.com/Keithtyy/INF1102-Lab