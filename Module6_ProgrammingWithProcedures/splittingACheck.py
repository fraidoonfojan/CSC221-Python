'''
Created on Nov 6, 2024

@author: fraidoon
'''
'''
Write a split_check function that returns the amount that each diner must pay to cover the cost of the meal.

The function has four parameters:

bill: The amount of the bill.
people: The number of diners to split the bill between.
tax_percentage: The extra tax percentage to add to the bill.
tip_percentage: The extra tip percentage to add to the bill.
The tax or tip percentages are optional and may not be given when calling split_check. Use default parameter values of 0.15 (15%) for tip_percentage, and 0.09 (9%) for tax_percentage. Assume that the tip is calculated from the amount of the bill before tax.

Sample output with inputs: 25 2

Cost per diner: $15.50
Sample output with inputs: 100 2 0.075 0.21

Cost per diner: $64.25

'''

def split_check(bill, people, tax_percentage=0.09, tip_percentage=0.15):
    # Calculate the tip and tax
    tip_amount = bill * tip_percentage
    tax_amount = bill * tax_percentage
    # Calculate the total bill
    total_bill = bill + tip_amount + tax_amount
    # Split the total bill between the diners
    cost_per_diner = total_bill / people
    return cost_per_diner

# Read inputs and call the function with default values
bill = float(input())
people = int(input())
print(f'Cost per diner: ${split_check(bill, people):.2f}')

# Read inputs and call the function with custom tax and tip percentages
bill = float(input())
people = int(input())
new_tax_percentage = float(input())
new_tip_percentage = float(input())
print(f'Cost per diner: ${split_check(bill, people, new_tax_percentage, new_tip_percentage):.2f}')