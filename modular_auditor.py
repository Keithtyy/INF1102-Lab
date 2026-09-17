inventory = 0
invalid_input = 0

def get_valid_input(stock):

    if stock.isnumeric() and int(stock) >= 0:
        return True

    if stock == "quit":
        print("Total units processed: ", inventory)
        print("Invalid inputs encountered: ", invalid_input)
        print("Exiting the program.")
        return stock

def process_delivery(current_value, new_value):
    current_value += new_value
    return current_value


while True:
    stock = input("Enter a stock quantity: ")

    if not get_valid_input(stock):
        print("Invalid input. Please enter a numeric value.")
        invalid_input += 1
    elif stock == "quit":
        break
    else:
        inventory = process_delivery(inventory, int(stock))
        print("Current stock quantity:", inventory)

#Link to github repo: https://github.com/Keithtyy/INF1102-Lab