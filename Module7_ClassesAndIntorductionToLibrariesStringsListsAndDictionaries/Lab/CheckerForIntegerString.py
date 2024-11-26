'''
Created on Nov 21, 2024

@author: fraidoon
'''
'''
Forms often allow a user to enter an integer. 
Write a program that takes in a string representing an integer as input, 
and outputs Yes if every character is a digit 0-9 or No otherwise.

Ex: If the input is:

1995
the output is:

Yes
Ex: If the input is:

42,000
or any string with a non-integer character, the output is:

No

'''

user_string = input()

if user_string.isdigit():  # Check if all characters are digits
    print("Yes")
else:
    print("No")