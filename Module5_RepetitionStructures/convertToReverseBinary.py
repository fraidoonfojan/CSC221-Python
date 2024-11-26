'''
Created on Oct 29, 2024

@author: fraidoon
'''
'''
Convert to reverse binary
Write a program that takes in a positive integer as input, and outputs a string of 1's and 0's representing the integer in reverse binary. For an integer x, the algorithm is

'''
x = int(input("Enter a positive integer: "))

# Initialize an empty string to store the result
reverse_binary = ""

# Loop until x is 0
while x > 0:
    # Append the remainder of x divided by 2 to reverse_binary
    reverse_binary += str(x % 2)
    # Update x by dividing it by 2
    x //= 2

# Output the result
print(reverse_binary)