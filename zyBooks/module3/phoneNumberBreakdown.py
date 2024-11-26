'''
Created on Oct 8, 2024

@author: fraidoon
'''

'''Given an integer representing a 10-digit phone number, output the area code, prefix, and line number using the format (800) 555-1212.

Ex: If the input is:

8005551212
the output is:

(800) 555-1212'''

# Input: Read the 10-digit phone number as a string to preserve leading zeros (if any)
phone_number = input()

# Extract the area code, prefix, and line number using string slicing
area_code = phone_number[:3]
prefix = phone_number[3:6]
line_number = phone_number[6:]

# Output the phone number in the desired format
print(f'({area_code}) {prefix}-{line_number}')