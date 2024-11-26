'''
Created on Oct 7, 2024

@author: fraidoon
'''
'''
Set colors_set1 contains 'olive'. Set colors_set2 contains two strings read from input. Perform the following tasks:

Update colors_set1 with colors_set2.
Remove 'orange' from colors_set1.
Read the next string from input and add the string to colors_set1.
'''
colors_set1 = {'olive'}
colors_set2 = set()
colors_set2.add(input())
colors_set2.add(input())

colors_set1.update(colors_set2)
colors_set1.remove('orange')
colors_set1.add(input())

print(f'colors_set1: {sorted(colors_set1)}')
print(f'colors_set2: {sorted(colors_set2)}')