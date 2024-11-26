'''
Created on Nov 19, 2024

@author: fraidoon
'''

'''
List iteration
A programmer accesses each element of a list. Thus, 
learning how to iterate through a list using a loop is critical.

Looping through a sequence such as a list is so common that Python 
supports a construct called a for loop, specifically for iteration purposes. 
The format of a for loop is shown below.


example: Iterating over a list

List measurements_list contains integers read from input, 
representing data samples from an experiment. 
For each element in measurements_list:

If the element's value is greater than 55, then 
output 'Sample ', followed by the element's index, and ' is abnormal'.
Otherwise, increment normal_samples and output 'Sample ', followed 
by the element's index, and ' is normal'.
'''

# Read input and split input into tokens
tokens = input().split()

# Convert tokens to integers and store in measurements_list
measurements_list = []
for token in tokens:
    measurements_list.append(int(token))

print(f'Raw samples: {measurements_list}')

# Initialize the counter for normal samples
normal_samples = 0

# Iterate through the measurements_list
for index, value in enumerate(measurements_list):
    if value > 55:  # Check if the sample is abnormal
        print(f'Sample {index} is abnormal')
    else:  # If normal, increment the counter and output normal
        normal_samples += 1
        print(f'Sample {index} is normal')

# Output the total number of normal samples
print(f'Total normal samples: {normal_samples}')