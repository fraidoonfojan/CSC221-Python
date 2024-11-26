'''
Created on Nov 19, 2024

@author: fraidoon
'''

'''
List basics
The list object type is one of the most important and often-used types in Python. 
Two terms that are used to define a list are container and mutable. 
A container is an object that groups related objects together. 
A list is a mutable container, meaning the size of the list can grow or shrink 
and elements within the list can change. A list is also a sequence; 
thus, the contained objects maintain a left-to-right positional order. 
Elements of the list can be accessed via indexing operations that 
specify the position of the desired element in the list. 
Each element in a list can be a different object type such as strings, 
integers, floats, or even other lists.


Six values are read from input and stored in the list list_data. Output 'List item: ' followed by the fourth element of list_data.

Click here for example
Ex: If the input is Vietnam 58 78 ivory rose 32, then the output is:
List item: ivory

'''

list_data = []
for elem in input().split():
    if elem.isdigit(): # If elem is a digit, then convert to int.
        list_data.append(int(elem))
    else:
        list_data.append(elem)

print(f'List item: {list_data[3]}')

