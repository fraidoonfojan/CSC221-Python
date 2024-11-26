'''
Created on Nov 20, 2024

@author: fraidoon
'''
'''
List num_list contains strings read from input. 
Use list comprehension to convert each string in num_list to an integer, 
and assign computed_list with the new list returned by list comprehension.

'''

num_list = []

# Read input
num_list = input().split()

# Use list comprehension to convert each string in num_list to an integer
computed_list = [int(number) for number in num_list]

print(f'Raw: {num_list}')
print(f'Computed: {computed_list}')