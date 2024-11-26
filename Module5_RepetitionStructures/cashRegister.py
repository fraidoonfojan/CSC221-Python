'''
Created on Oct 21, 2024

@author: fraidoon
'''
'''
CashRegister

Requirements Analysis (English Description)
Create a program that allows a user to calculate 
the amount due for items that a customer is
purchasing from a store. The program will ask
the user for the price of the item and if that 
item's price is greater than or equal to 0 that 
item's price will be added to the total. This
program should continue until the user enters a 
negative number. Once the user enters a negative 
number, the program will end by displaying the
total.
'''

# Initialize total to 0
total = 0

while True:
    # Step 1: Ask the user for the price of the item
    item_price = float(input("Enter the price of the item (negative number to stop): "))

    # Step 2: Check if the price is negative
    if item_price < 0:
        break  # Step 6: End the loop if the user enters a negative number

    # Step 3: Add the price of the item to the total
    total += item_price

    # Step 4 & 5: The loop will ask for the next item price

# Step 6: Print the total amount due
print(f"Total amount due: ${total:.2f}")

# Step 7: END