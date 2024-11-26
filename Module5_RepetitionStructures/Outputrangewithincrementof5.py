'''
Created on Oct 29, 2024

@author: fraidoon
'''
'''
Write a program whose input is two integers. Output the first integer and subsequent increments of 5 as long as the value is less than or equal to the second integer.

'''
# Take two integers as input
start = int(input("Enter the first integer: "))
end = int(input("Enter the second integer: "))

# Check if the second integer is less than the first
if end < start:
    print("Second integer can't be less than the first.")
else:
    # Loop from start to end, incrementing by 5 each time
    while start <= end:
        print(start, end=" ")
        start += 5
    print()  # End the output with a newline