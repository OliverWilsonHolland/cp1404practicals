"""
CP1404/CP5632 - Practical
A program that calculates the total price for a number of items
"""

number_of_items = int(input("Number of items: "))
total_price = 0
for i in range(0, number_of_items):
    item_price = float(input("Price of item: "))
    total_price = total_price + item_price
discount = total_price * 0.10
total_price = total_price - discount
# prints the float total price to 2 decimal places
print(f"Total price for {number_of_items} items is ${total_price:.2f}")