'''
Created on Nov 5, 2024

@author: fraidoon
'''
def c_to_f(temp_celsius):
    # Convert Celsius to Fahrenheit using the formula
    temp_fahrenheit = temp_celsius * 9 / 5 + 32
    return temp_fahrenheit

# Input for temperature in Celsius
temp_c = float(input('Enter temperature in Celsius: '))

# Call conversion function and assign result to temp_f
temp_f = c_to_f(temp_c)

# Print result
print(f'Fahrenheit: {temp_f}')