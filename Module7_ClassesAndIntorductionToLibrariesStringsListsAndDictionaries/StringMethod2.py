'''
Created on Nov 19, 2024

@author: fraidoon
'''
'''
Strings name1 and name2 are read from input. Write an if-else statement that compares the strings:

If name1 and name2 have exactly the same characters, output 'Same ASCII values'.
Otherwise, output the string with the smaller ASCII value.

'''
# Read input
name1 = input()
name2 = input()

# Compare the strings
if name1 == name2:
    print("Same ASCII values")
else:
    # Output the string with the smaller ASCII value
    print(min(name1, name2))