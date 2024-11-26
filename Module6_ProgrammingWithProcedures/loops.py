'''
Created on Nov 5, 2024

@author: fraidoon
'''
'''
Define a function find_employee_tax() that takes one parameter as a person's age, and returns the person's tax percent. The tax percent is returned as follows:

If the person's age is at least 60 years old, then the tax percent is 0.17.
If the person's age is more than 40 and less than 60 years old, then the tax percent is 0.27.
Otherwise, the tax percent is 0.37.
'''

def find_employee_tax(age):
    if age >= 60:
        return 0.17
    elif age > 40 and age < 60:
        return 0.27
    else:
        return 0.37

# Input user age
input_user_age = int(input())

# Testing function with specific age and user input
print(f'Testing 32: {find_employee_tax(32)}')
print(f'Testing user input: {find_employee_tax(input_user_age)}')