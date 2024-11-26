'''
Created on Nov 19, 2024

@author: fraidoon
'''
'''

Three strings are read from input and stored in the list names_data. Then, three more strings are read from input and stored in the list new_names. Create a new list called updated_names that contains the elements of names_data and new_names, in that order.

'''

# Read the first three strings and store them in names_data
names_data = input().split()

# Read the next three strings and store them in new_names
new_names = input().split()

# Create a new list updated_names that combines names_data and new_names
updated_names = names_data + new_names

# Output the resulting list
print(f"My names: {updated_names}")