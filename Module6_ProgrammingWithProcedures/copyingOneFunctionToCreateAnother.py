'''
Created on Nov 5, 2024

@author: fraidoon
'''
'''
Using the celsius_to_kelvin function as a guide, create a new function, changing the name to kelvin_to_celsius, and modifying the function accordingly.

Sample output with input: 283.15
10.0 C is 283.15 K
283.15 K is 10.0 C

'''

def celsius_to_kelvin(value_celsius):
    value_kelvin = value_celsius + 273.15
    return value_kelvin

def kelvin_to_celsius(value_kelvin):
    # Convert Kelvin to Celsius
    value_celsius = value_kelvin - 273.15
    return value_celsius

# Test the celsius_to_kelvin function
value_c = 10.0
print(f'{value_c} C is {celsius_to_kelvin(value_c)} K')

# Test the kelvin_to_celsius function
value_k = float(input())
print(f'{value_k} K is {kelvin_to_celsius(value_k)} C')