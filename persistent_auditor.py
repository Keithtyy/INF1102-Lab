def load_inventory():
    with open ("inventory.txt", "r") as file:
        content = file.readlines()
        inventory = int(content[-1])
        return inventory
    
def save_inventory(inventory, previous_transactions):
    with open("inventory.txt", "w") as file:
        file.write(f"All transactions this session: {previous_transactions} \n")
        file.write(f"Total inventory currently:\n")
        file.write(str(inventory))

def get_valid_input(stock):

    if stock.isnumeric() and int(stock) >= 0:
        return True

    if stock == "quit":
        generate_report(inventory, invalid_input)
        return stock

def process_delivery(current_value, new_value, previous_transactions):
    current_value += new_value
    previous_transactions.append(new_value)
    return current_value, previous_transactions

def calculate_tax(amount):
    tax_rate = 0.10
    tax_amount = int(amount) * tax_rate
    return tax_amount

def generate_report(inventory, invalid_input):
    print("Total units processed: ", inventory)
    print("Invalid inputs encountered: ", invalid_input)
    print("Exiting the program.")

invalid_input = 0
inventory = load_inventory()
previous_transactions = []

while True:

    if inventory >500:
        print("Overstock detected, cannot add more stocks")
        break

    stock = input("Enter a stock delivery quantity: ")

    if not get_valid_input(stock):
        print("Invalid input. Please enter a numeric value.")
        invalid_input += 1
    elif stock == "quit":
        save_inventory(inventory, previous_transactions)
        break
    else:
        inventory, previous_transactions = process_delivery(inventory, int(stock), previous_transactions)
        tax = calculate_tax(stock)
        print("Current stock quantity:", inventory)
        print("Tax amount on current delivery:", tax)

#Link to github repo: https://github.com/Keithtyy/INF1102-Lab