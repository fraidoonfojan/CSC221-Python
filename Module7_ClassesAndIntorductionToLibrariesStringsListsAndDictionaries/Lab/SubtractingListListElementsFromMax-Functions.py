'''
Created on Nov 21, 2024

@author: fraidoon
'''
'''
Subtracting list elements from max - functions
When analyzing data sets, such as data for human heights or for human 
weights, a common step is to adjust the data. This can be done by 
normalizing to values between 0 and 1, or throwing away outliers. 
For this program, adjust the values by subtracting each value from 
the maximum. Input values should be added to the list until -1 is entered.

Ex: If the input is:

30
50
10
70
65
-1
the output is:

40
20
60
0
5
Your program must define and call the function:
def get_max_int(nums)

Note: get_max_int() returns the maximum value in the list.

'''


def get_max_int(nums):
    # Return the maximum integer in the list
    return max(nums)

if __name__ == '__main__':
    nums = []
    
    # Read input until -1 is entered
    while True:
        value = int(input())
        if value == -1:
            break
        nums.append(value)
    
    # Get the maximum value in the list
    max_value = get_max_int(nums)
    
    # Adjust and print each value by subtracting it from the max
    for num in nums:
        print(max_value - num)