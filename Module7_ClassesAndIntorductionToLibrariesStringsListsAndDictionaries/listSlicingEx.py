'''
Created on Nov 19, 2024

@author: fraidoon
'''

'''
List experimental_data is read from input. 
The elements of experimental_data are separated into thirds. 
The first third of the data is collected in the morning, the second third in the afternoon, and the last third in the evening. Integer slice_length represents the number of data in each third.

Assign slice_length with len(experimental_data) // 3.
Assign morning_group with a slice of experimental_data 
from the beginning up to and excluding index slice_length.
Assign afternoon_group with a slice of experimental_data 
from index slice_length up to and excluding index (2 * slice_length).
Assign evening_group with a slice of experimental_data 
from index (2 * slice_length) up to and including the end.
'''

experimental_data = []
for token in input().split():
    experimental_data.append(int(token))

# Calculate the length of each slice
slice_length = len(experimental_data) // 3

# Create the groups by slicing
morning_group = experimental_data[:slice_length]
afternoon_group = experimental_data[slice_length:2 * slice_length]
evening_group = experimental_data[2 * slice_length:]

# Print the results
print(f'Number of data in each third: {slice_length}')
print(f'Complete data list: {experimental_data}')
print(f'Morning group: {morning_group}')
print(f'Afternoon group: {afternoon_group}')
print(f'Evening group: {evening_group}')