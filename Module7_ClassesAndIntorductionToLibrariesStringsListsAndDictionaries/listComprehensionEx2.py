'''
Created on Nov 20, 2024

@author: fraidoon
'''
'''

Integer num_rows is read from input, representing the number of rows 
in a two-dimensional list. List num_list is a two-dimensional 
list containing the remaining integers read from input. 
Assign computed_result with the total number of elements in num_list.

Ex: If the input is:
3
12 26 9
21 46 23 19
39 42 23

'''

# Read input
num_rows = int(input())
num_list = []
for i in range(num_rows):
    num_list.append([int(x) for x in input().split()])

# Calculate the total number of elements in num_list
computed_result = sum(len(row) for row in num_list)

print(f'All numbers: {num_list}')
print(f'Total number of elements: {computed_result}')