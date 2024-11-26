'''
Created on Oct 3, 2024

@author: fraidoon
'''
from _ast import In

print("Enter the cost of one credit")
costPerCredit = float(input())

print("Enter number of credit")
numOfCredits = int(input())

tuitionFees = costPerCredit * numOfCredits
print("Cost of one credit is $", costPerCredit)
print("number of credit per semester is", numOfCredits)
print("The cost of tuition this semester is $", tuitionFees)
print(f"{tuitionFees:.2f}") # formatting output results in Python. 2f is 2 decimal number and f is float