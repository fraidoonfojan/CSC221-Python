'''
Created on Nov 21, 2024

@author: fraidoon
'''
'''
A palindrome is a word or a phrase that is the same when read both forward 
and backward. Examples are: "bob," "sees," or "never odd or even" 
(ignoring spaces). Write a program whose input is a word or phrase, 
and that outputs whether the input is a palindrome.

Ex: If the input is:

bob
the output is:

palindrome: bob
Ex: If the input is:

bobby
the output is:

not a palindrome: bobby
Hint: Start by removing spaces. Then check if the string equals itself in reverse.

'''

# Read input
user_input = input()

# Remove spaces and convert to lowercase for case insensitivity
normalized_input = user_input.replace(" ", "").lower()

# Check if the input is equal to its reverse
if normalized_input == normalized_input[::-1]:
    print(f"palindrome: {user_input}")
else:
    print(f"not a palindrome: {user_input}")