'''
Created on Nov 21, 2024

@author: fraidoon
'''
'''

A function defined within a class is known as an instance method. 
An instance method can be referenced using dot notation. 
The following example illustrates:

Example:
box1 and box2 are instances of the Box class. 
Attributes length, width, and height of both box1 and box2 are read from input. 
In the Box class, define instance method get_volume() with self as 
the parameter to return the product of attributes length, width, and height

'''

class Box:
    def __init__(self):
        self.length = 0
        self.width = 0
        self.height = 0

    def get_volume(self):
        return self.length * self.width * self.height

# Create two Box instances
box1 = Box()
box2 = Box()

# Read input and assign attributes for box1
box1.length = int(input())
box1.width = int(input())
box1.height = int(input())

# Read input and assign attributes for box2
box2.length = int(input())
box2.width = int(input())
box2.height = int(input())

# Output volumes of the two boxes
print(f"First box's volume: {box1.get_volume()}")
print(f"Second box's volume: {box2.get_volume()}")