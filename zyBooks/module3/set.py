'''
Created on Oct 7, 2024

@author: fraidoon
'''

'''
A set is an unordered collection of unique elements. A set has the following properties:
Elements are unordered: Elements in the set do not have a position or index.
Elements are unique: No elements in the set share the same value.
A set can be created using the set() function, which accepts a sequence-type iterable object (list, tuple, string, etc.) whose elements are inserted into the set. A set literal can be written using curly braces { } with commas separating set elements. Note that an empty set can only be created using set().
'''
# Initial list contains some duplicate values
first_names = [ 'Alba', 'Hema', 'Ron', 'Alba', 'Musa', 'Ron', 'Ron' ]

# Creating a set removes any duplicate values
names_set = set(first_names)

print(names_set)

nums = [1, 4, 2,7 , 9, 0, 21]
nums_set = set(nums)
print(nums_set)
sett = set([10, 20, 25])
print(sett)