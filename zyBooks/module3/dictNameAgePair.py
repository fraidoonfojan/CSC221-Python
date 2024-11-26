'''
Created on Oct 9, 2024

@author: fraidoon
'''
'''
Dictionary name_age_pairs contains four key-value pairs. Read a string from input, representing a key found in name_age_pairs. Then, assign the value associated with the key read with the current value minus 3.

'''

# Given dictionary with name and age pairs
name_age_pairs = {'Mel': 15, 'Fay': 22, 'Zoe': 32, 'Avi': 36}

# Output the original dictionary
print('Original:')
print(name_age_pairs)

# Input: Read the name (key) from the user
name = input()

# Subtract 3 from the value associated with the key (name)
name_age_pairs[name] = name_age_pairs[name] - 3

# Output the updated dictionary
print('Updated:')
print(name_age_pairs)