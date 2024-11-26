'''
Created on Nov 21, 2024

@author: fraidoon
'''
'''
The Profile class constructor has a self parameter and two additional parameters: 
age and status. profile1 is created with 36 and 'idle' as the values of the 
two attributes in that order. profile2 is created with the values of the 
two attributes read from input. 
Complete the constructor so the instance attributes are assigned.

Click here for example
Ex: If the input is:
44
active

'''
class Profile:
    def __init__(self, age, status):
        # Assign instance attributes
        self.age = age
        self.status = status

age2 = int(input())
status2 = input()

# Create instances of Profile
profile1 = Profile(36, 'idle')
profile2 = Profile(age2, status2)

# Output profile data
print(f'profile1 data: {profile1.age} years old, {profile1.status}')
print(f'profile2 data: {profile2.age} years old, {profile2.status}')