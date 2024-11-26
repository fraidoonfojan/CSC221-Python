'''
Created on Oct 29, 2024

@author: fraidoon
'''
'''
Create a program that allows a user to find the sum of exactly five numbers.
The user will be prompted for one number at a time. After the user enters 
five numbers, the program should display the sum of these five numbers.
'''
print('This program will find the sum of exactly five numbers')

# Initialize the total to 0
total = 0

# Loop exactly five times to get five numbers
for i in range(5):
    # Prompt the user for each number and add it to the total
    num = int(input(f'Please enter number {i + 1}: '))
    total += num

# Output the total sum of the five numbers
print(f'The total is: {total}')
