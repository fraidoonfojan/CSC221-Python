'''
Created on Oct 29, 2024

@author: fraidoon
'''
'''
Many user-created passwords are simple and easy to guess. Write a program that takes a simple password and makes it stronger by replacing characters using the key below, and by appending "!" to the end of the input string.

i becomes 1
a becomes @
m becomes M
B becomes 8
s becomes $
'''

# Take a simple password as input
password = input("Enter a password: ")

# Initialize an empty string to build the stronger password
strong_password = ""

# Iterate over each character in the original password
for char in password:
    # Replace characters according to the given rules
    if char == 'i':
        strong_password += '1'
    elif char == 'a':
        strong_password += '@'
    elif char == 'm':
        strong_password += 'M'
    elif char == 'B':
        strong_password += '8'
    elif char == 's':
        strong_password += '$'
    else:
        strong_password += char  # Keep the character as is if no replacement

# Append "!" to the end of the stronger password
strong_password += "!"

# Output the stronger password
print(strong_password)