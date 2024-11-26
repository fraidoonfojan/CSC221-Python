'''
Created on Oct 16, 2024

@author: fraidoon
'''
'''
Small towns have populations in the range 1100 - 4950 inclusive. Write an if statement that outputs 'Not a small town' if the input num_residents is not in this range. Otherwise, output 'Small town'.

'''
num_residents = int(input())

if 1100 <= num_residents <= 4950:
    print("Small town")
else:
    print("Not a small town")