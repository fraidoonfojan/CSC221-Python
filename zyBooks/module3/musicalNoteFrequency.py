'''
Created on Oct 8, 2024

@author: fraidoon
'''
import math

# Input: Read the initial frequency f0
f0 = float(input())

# Define the frequency ratio r
r = 2 ** (1 / 12)

# Calculate the frequencies of the next 3 higher keys
f1 = f0 * r
f2 = f0 * (r ** 2)
f3 = f0 * (r ** 3)

# Output the results rounded to 2 decimal places followed by "Hz"
print(f'{f0:.2f} Hz')
print(f'{f1:.2f} Hz')
print(f'{f2:.2f} Hz')
print(f'{f3:.2f} Hz')