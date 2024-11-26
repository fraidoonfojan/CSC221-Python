'''
Created on Oct 8, 2024

@author: fraidoon
'''
'''
Given 4 floating-point numbers. Use a string formatting expression with conversion specifiers to output their product and their average as integers (rounded), then as floating-point numbers.

Output each rounded integer using the following:
print(f'{your_value:.0f}')

Output each floating-point value with three digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.3f}')

Ex: If the input is:

8.3
10.4
5.0
4.8
'''
# Input: Read four floating-point numbers
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

# Calculate the product of the four numbers
product = num1 * num2 * num3 * num4

# Calculate the average of the four numbers
average = (num1 + num2 + num3 + num4) / 4

# Output the product and average as rounded integers
print(f'{product:.0f} {average:.0f}')

# Output the product and average as floating-point numbers with 3 decimal places
print(f'{product:.3f} {average:.3f}')