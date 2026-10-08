# Complete the TODOs using the Python concepts introduced in class.
# Run this file to check your result.  

# DG8002 - F26 - Activity 4
# Author Name: Susel Naranjo Vega
# Date: October 7th, 2026

# SCENARIO
# A restauraunt wants a simple ordering system that allows customers to browse a menu, select items, and calculate their total bill.

menu  = {
    "Burger" : 12.00,
    "Pizza" : 15.00,
    "Salad" : 9.00,
    "Fries" : 5.00,
    "Drink" : 3.00
}

order = []

# TODO 1: Print out the entire menu and the price of each item
print("Restaurant Menu")

for item, price in menu.items():
    print(f"{item}: ${price:.2f}")
# TODO 2: Start a loop, asking the customer which item they would like to order
while True:
    customer_choice = input("What would you like to order? (Type Done to finish): ").strip()
    # TODO 3: If the customer types a word check whether the requested item exists
    if customer_choice in menu:
    # TODO 4: Add valid items to the customer's order and let the loop continue
        order.append(customer_choice)
        print(f"{customer_choice} added to your order!")
    # TODO 5: if the customer types "Done", end the loop and move to end of order
    elif customer_choice.lower() == "done":
        break
    else:
        print("Sorry, that item is not on the menu. Please try again.")
# TODO 6: Print out an itemized receipt for the user showing item and cost
print("\nYour Receipt")

subtotal = 0

for item in order:
    price = menu[item]
    print(f"{item}: ${price:.2f}")
    subtotal += price
# TODO 7: Print out the subtotal of the entire order
print(f"TOTAL: ${subtotal:.2f}")

# EXPECTED OUTPUT
# Order: Burger - 12.00
#        Fries  -  5.00
#        Drink  -  3.00
#         TOTAL: $20.00
