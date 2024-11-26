'''
Created on Nov 21, 2024

@author: fraidoon
'''
'''
Input values status1, username1 and age1 are read from input, 
representing the status, username, and age of a profile. 
An element representing a new status is also read from input as new_status. 
Complete the following tasks:

Assign profile1 with an instance of Profile with status1, 
username1 and age1 as attributes in that order.
Call profile1's print_data().
Call profile1's update_status() with argument new_status.
Call profile1's print_data() again.
Ex: If the input is:
idle
gray-elk
25
active

'''

class Profile:
    def __init__(self, status, username, age): 
        self.status = status
        self.username = username
        self.age = age

    def update_status(self, new_status):
        self.status = new_status

    def print_data(self):
        print(f'Profile data: {self.status}, user {self.username}, {self.age} years old')

status1 = input()
username1 = input()
age1 = int(input())
new_status = input()

# Create an instance of Profile
profile1 = Profile(status1, username1, age1)

# Call print_data method
profile1.print_data()

# Call update_status method
profile1.update_status(new_status)

# Call print_data method again
profile1.print_data()