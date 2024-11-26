'''
Created on Oct 29, 2024

@author: fraidoon
'''
'''
Integer cardigan_count is initialized with 0. String next_item is read from input. Write a loop that iterates while next_item is not equal to 'Over'. In each iteration of the loop:

'''

cardigan_count = 0
next_item = input()

# Loop continues as long as next_item is not 'Over'
while next_item != 'Over':
    # Increment cardigan_count if next_item is 'Cardigan'
    if next_item == 'Cardigan':
        cardigan_count += 1
    # Read the next item from input
    next_item = input()

# Output the final count of 'Cardigan'
print(f'Cardigan occurs {cardigan_count} time(s).')