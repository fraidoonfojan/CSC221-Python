'''
Created on Nov 21, 2024

@author: fraidoon
'''
'''

Class and instance object types
A program with user-defined classes contains two additional types of objects: 
class objects and instance objects. 
A class object acts as a factory that creates instance objects. 
When created by the class object, an instance object is initialized 
via the __init__ method. The following tool demonstrates 
how the __init__ method of the Time class object is used to 
initialize two new Time instance objects:

A class attribute is shared among all instances of that class. 
Class attributes are defined within the scope of a class.


Example: Define a class attribute named m_in_words in the Length class, 
and assign m_in_words with 'meters'.

Ex: If the input is 49, then the output is:

49 meters

'''

class Length:
    # Define a class attribute
    m_in_words = 'meters'

    def __init__(self, meters):
        self.meters = meters

# Read input for length in meters
length_value = int(input())

# Create an instance of Length
length = Length(length_value)

# Output the length with the class attribute
print(f'{length.meters} {Length.m_in_words}')



