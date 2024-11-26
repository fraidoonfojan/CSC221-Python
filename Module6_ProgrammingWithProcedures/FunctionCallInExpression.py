'''
Created on Nov 5, 2024

@author: fraidoon
'''
'''

Assign max_sum with the greater of num_a and num_b, PLUS the greater of num_y and num_z. Use just one statement. Hint: Call find_max() twice in an expression.

Sample output with inputs: 5.0 10.0 3.0 7.0
max_sum is: 17.0
'''

def find_max(num_1, num_2):
    if num_1 > num_2:
        max_val = num_1
    else:
        max_val = num_2
    return max_val

# Initialize max_sum to 0.0
max_sum = 0.0

# Read inputs
num_a = float(input())
num_b = float(input())
num_y = float(input())
num_z = float(input())

# Calculate max_sum in one statement
max_sum = find_max(num_a, num_b) + find_max(num_y, num_z)

# Output the result
print(f'max_sum is: {max_sum}')