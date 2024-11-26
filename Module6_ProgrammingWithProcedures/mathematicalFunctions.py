'''
Created on Nov 5, 2024

@author: fraidoon
'''
'''

Complete the function convert_to_centimeters() that has one parameter as a length in inches. The function returns the length converted to centimeters, given that 1 inch = 2.54 centimeters.

Ex: If the input is 26, then the output is:

Centimeters: 66.040
'''
IN_TO_CM = 2.54

def convert_to_centimeters(user_inches):
    # Convert inches to centimeters
    return user_inches * IN_TO_CM

num_inches = int(input())

# Print with value rounded to 3 decimal places
print(f'Centimeters: {convert_to_centimeters(num_inches):.3f}')