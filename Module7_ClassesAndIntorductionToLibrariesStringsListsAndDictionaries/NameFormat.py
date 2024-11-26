'''
Created on Nov 21, 2024

@author: fraidoon
'''
'''
Many documents use a specific format for a person's name. 
Write a program that reads a person's name in the following format:

firstName middleName lastName (in one line)

and outputs the person's name in the following format:

lastName, firstInitial.middleInitial.

Ex: If the input is:

Pat Silly Doe
the output is:

Doe, P.S.
If the input has the following format:

firstName lastName (in one line)

the output is:

lastName, firstInitial.

Ex: If the input is:

Julia Clark
the output is:

Clark, J.

'''

name_parts = input().split()

if len(name_parts) == 3:  # First, middle, and last name
    first_name, middle_name, last_name = name_parts
    print(f"{last_name}, {first_name[0]}.{middle_name[0]}.")
elif len(name_parts) == 2:  # First and last name only
    first_name, last_name = name_parts
    print(f"{last_name}, {first_name[0]}.")
else:
    print("Invalid input format")