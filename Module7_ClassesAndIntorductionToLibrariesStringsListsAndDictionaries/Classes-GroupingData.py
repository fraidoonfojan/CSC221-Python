'''
Created on Nov 21, 2024

@author: fraidoon
'''
'''
Multiple variables are frequently closely related and should be treated 
as one variable with multiple parts. For example, two variables called 
hours and minutes might be grouped together in a single variable called time. 
The class keyword can be used to create a user-defined type of object 
containing groups of related variables and functions.


A class defines a new type that can group data and functions to form an object. 
The object maintains a set of attributes that determines the data and 
behavior of the class. For example, the following code defines a new class 
containing two attributes, hours and minutes, whose values are initially 0:

example: Define a class named EmployeeDetails that contains the 
attributes age and id. Initialize age and id with 0.

'''

# Define the EmployeeDetails class
class EmployeeDetails:
    def __init__(self):
        self.age = 0
        self.id = 0

my_employee = EmployeeDetails()

print('Employee details (before):', end=' ')
print(f'{my_employee.age} years old,', end=' ')
print(f'#{my_employee.id}')

my_employee.age = int(input())
my_employee.id = int(input())

print('Employee details (after):', end=' ')
print(f'{my_employee.age} years old,', end=' ')
print(f'#{my_employee.id}')