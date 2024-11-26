'''
Created on Oct 7, 2024

@author: fraidoon
'''
# Create sets

names1 = {'Corrin', 'Pedro', 'Khan', 'Dean'}
names2 = {'Emilia', 'Kara', 'Corrin', 'Tia'}
names3 = {'Karat', 'Kara', 'Karah', 'Khan'}
names4 = {'Khan', 'Dean', 'Pascale'}

# Union names1 and names2
result_set = names1.union(names2)

# Intersection btwn result_set and names3
result_set = result_set.intersection(names3)

# Difference btwn result_set and names4
result_set = result_set.difference(names4)
print(result_set)