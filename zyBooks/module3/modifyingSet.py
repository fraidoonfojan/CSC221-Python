'''
Created on Oct 7, 2024

@author: fraidoon
'''
'''
Modifying sets
Sets are mutable – elements can be added or removed using set methods. The add() method places a new element into the set if the set does not contain an element with the provided value. The remove() and pop() methods remove an element from the set.

Additionally, sets support the len() function to return the number of elements in a set. To check if a specific value exists in a set, a membership test such as value in set (discussed in another section) can be use
'''

# Create sets
names1 = {'Pedro', 'Khan', 'Dean'}
names2 = {'Emilia', 'Kara', 'Tia'}

# Add element to set
names1.add('Hyungu')

# Add names2 to names1
names1.update(names2)

# Remove element from set
names1.remove('Dean')

# Clear all elements from set
names2.clear()

