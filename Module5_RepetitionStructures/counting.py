'''
Created on Oct 29, 2024

@author: fraidoon
'''
'''
Integer num_threshold is read from input. Integer j is initialized with 8. Complete the while loop to perform the following tasks at each iteration until j is greater than num_threshold:

Increment j.
If j is divisible by 2, then output the value of j.

'''
num_threshold = int(input())
j = 8

while j <= num_threshold:
    # Increment j
    j += 1
    
    # Check if j is divisible by 2
    if j % 2 == 0:
        # Output the value of j
        print(j)