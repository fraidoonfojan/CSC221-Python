'''
Created on Oct 15, 2024

@author: fraidoon
'''


import math

# Function to calculate the total cost for one order
def calculate_order(carpet_price_per_sqft, room_width, room_length, order_number):
    # Calculate room area and carpet cost
    room_area = room_width * room_length
    carpet_cost = round(carpet_price_per_sqft * room_area * 1.20, 2)  # 20% extra for waste
    
    # Calculate labor cost
    labor_cost = round(room_area * 0.75, 2)
    
    # Calculate sales tax (7%)
    sales_tax = round(0.07 * (carpet_cost + labor_cost), 2)
    
    # Calculate total cost (carpet + labor + tax)
    total_cost = round(carpet_cost + labor_cost + sales_tax, 2)
    
    # Output details for the order
    print(f"Order #{order_number}")
    print(f"Room: {room_area} sq ft")
    print(f"Carpet: ${carpet_cost:.2f}")
    print(f"Labor: ${labor_cost:.2f}")
    print(f"Tax: ${sales_tax:.2f}")
    print(f"Cost: ${total_cost:.2f}")
    
    return total_cost

# Main program for three orders
def main():
    # Read input for the first order
    carpet_price1, room_width1, room_length1 = map(float, input().split())
    total_sales = calculate_order(carpet_price1, int(room_width1), int(room_length1), 1)
    
    # Add a blank line between orders
    print()
    
    # Read input for the second order
    carpet_price2, room_width2, room_length2 = map(float, input().split())
    total_sales += calculate_order(carpet_price2, int(room_width2), int(room_length2), 2)
    
    # Add a blank line between orders
    print()
    
    # Read input for the third order
    carpet_price3, room_width3, room_length3 = map(float, input().split())
    total_sales += calculate_order(carpet_price3, int(room_width3), int(room_length3), 3)

    # Add a blank line before total sales
    print()
    
    # Output the total sales for all three orders (explicitly rounding to 2 decimals)
    total_sales = round(total_sales, 2)
    print(f"Total Sales: ${total_sales:.2f}")

# Call the main function
main()