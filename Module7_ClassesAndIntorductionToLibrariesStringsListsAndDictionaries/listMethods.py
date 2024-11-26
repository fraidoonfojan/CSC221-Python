'''
Created on Nov 19, 2024

@author: fraidoon
'''
'''
Common list methods
A list method can perform a useful operation on a list such as adding 
or removing elements, sorting, reversing, etc.

The table below shows the available list methods. 
Many of the methods perform in-place modification of the list 
contents — a programmer should be aware that a method that modifies 
the list in-place changes the underlying list object, and thus 
may affect the value of a variable that references the object.


Ex.
Integer num_tourists is read from input, 
representing the number of strings to be read next. 
Read the remaining strings from input and append each string to tourists_list.
'''

# Read the number of tourists
num_tourists = int(input())

# Initialize an empty list to store tourist names
tourists_list = []

# Read num_tourists strings and append each to tourists_list
for _ in range(num_tourists):
    tourists_list.append(input())

# Output the resulting list
print(tourists_list)