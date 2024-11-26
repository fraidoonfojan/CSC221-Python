'''
Created on Nov 20, 2024

@author: fraidoon
'''
'''
A programmer modifies every element of a list in the same way, s
uch as adding 10 to every element. The Python language provides 
a convenient construct, known as list comprehension, 
that iterates over a list, modifies each element, and 
returns a new list of the modified elements.

A list comprehension has three components:

An expression component to evaluate for each element in the iterable object.
A loop variable component to bind to the current iteration element.
An iterable object component to iterate over (list, string, tuple, enumerate, etc).

Example: List data_list contains integers read from input. 
Assign list_times_five with a new list where each element is five times 
he corresponding element in data_list.

'''

data_list = []

# Read input
tokens = input().split()
for token in tokens:
    data_list.append(int(token))

# Create a new list where each element is five times the corresponding element in data_list
list_times_five = [number * 5 for number in data_list]

print(f'Original: {data_list}')
print(f'Every element times five: {list_times_five}')
