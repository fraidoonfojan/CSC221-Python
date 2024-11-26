'''
Created on Oct 15, 2024

@author: fraidoon
'''
import math

# Function to calculate the cost for a party
def calculate_party_cost(people, slices_per_person, cost_per_pizza, party_name):
    # Calculate the total number of slices needed
    total_slices_needed = people * slices_per_person
    
    # Calculate the number of pizzas (each pizza has 8 slices)
    pizzas_needed = math.ceil(total_slices_needed / 8)
    
    # Calculate the total cost of the pizzas
    total_cost_pizzas = pizzas_needed * cost_per_pizza
    
    # Calculate the tax (7% of pizza cost)
    tax = round(0.07 * total_cost_pizzas, 2)
    
    # Calculate the delivery charge (20% of cost including tax)
    delivery = round(0.20 * (total_cost_pizzas + tax), 2)
    
    # Calculate the total cost
    total_cost = round(total_cost_pizzas + tax + delivery, 2)
    
    # Output the results
    print(f"{party_name} Party")
    print(f"{pizzas_needed} Pizzas: ${total_cost_pizzas:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Delivery: ${delivery:.2f}")
    print(f"Total: ${total_cost:.2f}")
    
    return total_cost

# Read input for Friday night party (all values in one line)
input_data1 = input().split()
people1 = int(input_data1[0])
slices_per_person1 = float(input_data1[1])
cost_per_pizza1 = float(input_data1[2])
friday_total = calculate_party_cost(people1, slices_per_person1, cost_per_pizza1, "Friday Night")

# Add a blank line for separation
print()

# Read input for Saturday night party (all values in one line)
input_data2 = input().split()
people2 = int(input_data2[0])
slices_per_person2 = float(input_data2[1])
cost_per_pizza2 = float(input_data2[2])
saturday_total = calculate_party_cost(people2, slices_per_person2, cost_per_pizza2, "Saturday Night")

# Add a blank line for separation
print()

# Read input for Sunday night party (all values in one line)
input_data3 = input().split()
people3 = int(input_data3[0])
slices_per_person3 = float(input_data3[1])
cost_per_pizza3 = float(input_data3[2])
sunday_total = calculate_party_cost(people3, slices_per_person3, cost_per_pizza3, "Sunday Night")

# Add a blank line for separation
print()

# Calculate the weekend total
weekend_total = round(friday_total + saturday_total + sunday_total, 2)
print(f"Weekend Total: ${weekend_total:.2f}")