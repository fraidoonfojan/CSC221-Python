'''
Created on Nov 20, 2024

@author: fraidoon
'''
'''
Sometimes a program iterates over a list while modifying the elements, 
such as changing some elements' values or moving elements' positions.


Example: List data_list contains integers read from input. 
Each integer represents a random data sample in an experiment. 
Write a loop to remove every element from data_list that is 
less than or equal to 20.

'''

data_list = []

tokens = input().split()
for token in tokens:
    data_list.append(int(token))
  
print('Original samples:', end=' ')
for samples in data_list:
    print(samples, end=' ')
print()

# Filter out elements less than or equal to 20
for sample in data_list[:]:  # Iterate over a copy of data_list
    if sample <= 20:
        data_list.remove(sample)

print('Filtered samples:', end=' ')
for samples in data_list:
    print(samples, end=' ')
print()

