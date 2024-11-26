'''
Created on Nov 21, 2024

@author: fraidoon
'''
'''
Given a sorted list of integers, output "Middle item: " followed by 
the middle integer. Assume the number of integers is always odd.

Ex: If the input is:

2 3 4 8 11
the output is:

Middle item: 4
The maximum number of inputs for any test case should not exceed 9. 
If exceeded, output "Too many inputs".

Hint: First read the data into a list. Then, based on the list's size, 
find the middle item.

'''
# Read input and split into a list of integers
numbers = list(map(int, input().split()))

# Check if the number of inputs exceeds 9
if len(numbers) > 9:
    print("Too many inputs")
else:
    # Find the middle item (list is sorted by input assumption)
    middle_index = len(numbers) // 2
    print(f"Middle item: {numbers[middle_index]}")