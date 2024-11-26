'''
Created on Oct 29, 2024

@author: fraidoon
'''
'''
Positive integer num_insects is read from input. Write a while loop that in each iteration first prints and then doubles num_insects. The loop executes while values are less than or equal to 100. Output each number on a newline.

'''
num_insects = int(input())

while num_insects <= 100:
    print(num_insects)  
    num_insects *= 2 
