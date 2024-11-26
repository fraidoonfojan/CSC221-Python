'''
Created on Oct 8, 2024

@author: fraidoon
'''
# Input: Read the 10-digit phone number as an integer
phone_number = int(input())

# Extract the area code, prefix, and line number using // and %
area_code = phone_number // 10000000            # Get the first 3 digits (area code)
prefix = (phone_number // 10000) % 1000         # Get the next 3 digits (prefix)
line_number = phone_number % 10000              # Get the last 4 digits (line number)

# Output the phone number in the desired format
print(f'({area_code}) {prefix}-{line_number}')