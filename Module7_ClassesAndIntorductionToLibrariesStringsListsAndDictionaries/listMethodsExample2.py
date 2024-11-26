'''
Created on Nov 19, 2024

@author: fraidoon
'''
'''


List readings_list is read from input, representing a data 
sequence collected from an experiment. 
List readings_list has an odd number of elements. Perform the following tasks:

Sort readings_list in-place.
Reverse readings_list in-place.
Assign median_index with the size of readings_list divided by 2 
using floor division.
Assign expt_median with the value at median_index in readings_list.
'''

tokens = input().split()
readings_list = []
for token in tokens:
    readings_list.append(int(token))

# Sort readings_list in-place
readings_list.sort()

# Reverse readings_list in-place
readings_list.reverse()

# Calculate the median index using floor division
median_index = len(readings_list) // 2

# Assign the value at median_index to expt_median
expt_median = readings_list[median_index]

# Print the results
print(f'Sorted data: {readings_list}')
print(f'Median: {expt_median}')