
print("Menu:\n(I)nstructions\n(C)alculate\n(Q)uit")
choice = input("Choice: ").upper()

while choice != "Q":
    if choice == "I":
        print("Enter the number of products you want to buy and your chosen price.\nIf you buy 0-5 items, they're full price, over 5 items and each one is 10% off!")
    elif choice == "C":
        no_of_products = int(input("Number of products: "))
        while no_of_products < 0:
            print("Invalid number of products")
            no_of_products = int(input("Number of products: "))
        price = float(input("Price: $"))
        while price < 0:
            print("Invalid price")
            price = float(input("Price: $"))
        final_price = no_of_products * price
        if no_of_products > 5:
            final_price = no_of_products * price * 0.9
        print("Total price = ${} x {} products = ${}".format(price, no_of_products, final_price))
    else:
        print("Invalid Choice.")
    print("Menu:\n(I)nstructions\n(C)alculate\n(Q)uit")
    choice = input("Choice: ").upper()
print("Farewell Francis")
