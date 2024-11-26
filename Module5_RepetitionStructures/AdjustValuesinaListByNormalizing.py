'''
Created on Oct 29, 2024

@author: fraidoon
'''
'''
When analyzing data sets, such as data for human heights or for human weights, a common step is to adjust the data. This adjustment can be done by normalizing to values between 0 and 1, or throwing away outliers.

For this program, adjust the values by dividing all values by the largest value. The input begins with an integer indicating the number of floating-point values that follow. Assume that the list will always contain positive floating-point values.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')
'''

# Read the number of floating-point values
num_values = int(input())

# Initialize an empty list to store the values
values = []

# Read each floating-point value and add it to the list
for _ in range(num_values):
    values.append(float(input()))

# Find the maximum value in the list for normalization
max_value = max(values)

# Normalize each value by dividing by the maximum value and output the result
for value in values:
    normalized_value = value / max_value
    print(f'{normalized_value:.2f}')