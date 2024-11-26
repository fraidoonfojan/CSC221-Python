'''
Created on Nov 6, 2024

@author: fraidoon
'''
'''
phrase_list is read from input. print_swap() has one parameter list_to_modify, and swaps the first and last elements of list_to_modify. Call print_swap() with a copy of the list phrase_list as the argument to avoid modifying phrase_list.


'''

def print_swap(list_to_modify):
    # Swap the first and last elements
    temp = list_to_modify[0]
    list_to_modify[0] = list_to_modify[-1]
    list_to_modify[-1] = temp
    print(f'Swapped: {list_to_modify}')

# Read input and split into a list
phrase_list = input().split()

# Call print_swap() with a copy of phrase_list
print_swap(phrase_list.copy())

# Print the original list to show it remains unchanged
print(f'Original: {phrase_list}')