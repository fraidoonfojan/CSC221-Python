'''
Created on Oct 16, 2024

@author: fraidoon
'''
'''
An if-else statement subtracts 2 from allowed_groups if object_count <= 17 is True, or subtracts 5 from remaining_groups otherwise.

'''
object_count = int(input())
allowed_groups = int(input())
remaining_groups = int(input())

# Check if object_count is less than or equal to 17
if object_count <= 17:
    allowed_groups -= 2  # Subtract 2 from allowed_groups
else:
    remaining_groups -= 5  # Subtract 5 from remaining_groups

# Output the updated values
print(allowed_groups)
print(remaining_groups)