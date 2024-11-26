'''
Created on Oct 8, 2024

@author: fraidoon
'''
import math
# Read floating-point numbers from input
x = float(input())
y = float(input())
z = float(input())

# Perform the calculations
x_pow_z = x ** z                    # x^z
x_pow_z_pow_y = x ** y ** z       
abs_diff = abs(x - y)                # absolute difference between x and y
xz = x * z                           # x * z
sqrt_xz = math.sqrt(xz)              # square root of x * z

# Output the results formatted with two decimal places
print(f'{x_pow_z:.2f} {x_pow_z_pow_y:.2f} {abs_diff:.2f} {sqrt_xz:.2f}')