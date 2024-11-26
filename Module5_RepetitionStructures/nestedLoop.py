'''
Created on Oct 29, 2024

@author: fraidoon
'''
'''
Given num_rows and num_cols representing the number of rows and columns, write nested loops using range() to print a rectangle as shown in the example below.


'''

num_rows = int(input())
num_cols = int(input())

for i in range(num_rows):
    for j in range(num_cols):

        print('*', end=' ')
    print()