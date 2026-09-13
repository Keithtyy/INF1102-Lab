inventory = 0
invalid_input = 0
while True:
    if inventory > 500:
        print("Overstock detected, cannot add more stocks")
        break
    
    stock = input("Enter current stock quantity: ")

    if stock == "quit":
        print("Total units processed: ", inventory)
        print("Invalid inputs encountered: ", invalid_input)
        print("Exiting the program.")
        break

    if not stock.isnumeric() or int(stock) < 0:
        print("Invalid input. Please enter a numeric value.")
        invalid_input += 1
    
    else:
        inventory += int(stock)
        print("Current stock quantity: ", inventory)