'''
Created on Nov 21, 2024

@author: fraidoon
'''
'''
A class instance is initialized to a specific state. 
The __init__ method constructor can be customized with additional parameters.
Constructor parameters can have default values like any other function 
using the name=value syntax. Default parameter values may indicate 
the default state of an instance. A programmer might then use 
constructor arguments only to modify the default state if necessary.

Example:
Write a constructor with parameters self, num_mins and num_messages. 
num_mins and num_messages should have a default value of 0.

Sample output with one plan created with input 200 300, one plan 
created with no input, and one plan created with input 500.
My plan... Mins: 200 Messages: 300
Dad's plan... Mins: 0 Messages: 0
Mom's plan... Mins: 500 Messages: 0 
'''

class PhonePlan:
    def __init__(self, num_mins=0, num_messages=0):
        self.num_mins = num_mins
        self.num_messages = num_messages

    def print_plan(self):
        print(f'Mins: {self.num_mins}', end=' ')
        print(f'Messages: {self.num_messages}')


my_plan = PhonePlan(int(input()), int(input()))
dads_plan = PhonePlan()
moms_plan = PhonePlan(int(input()))

print('My plan...', end=' ')
my_plan.print_plan()

print('Dad\'s plan...', end=' ')
dads_plan.print_plan()

print('Mom\'s plan...', end=' ')
moms_plan.print_plan()