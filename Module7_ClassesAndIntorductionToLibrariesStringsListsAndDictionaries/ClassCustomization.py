'''
Created on Nov 21, 2024

@author: fraidoon
'''
'''
Class customization is the process of defining how an instance of a class 
should behave for some common operations. Such operations might 
include printing, accessing attributes, or how instances of that 
class are compared to each other. To customize a class, 
a programmer implements instance methods with special method names 
that the Python interpreter recognizes. 
Ex: To change how a class instance object is printed, 
the special __str__() method can be defined, as illustrated below.


Example:

Write the special method __str__() for CarRecord.

Sample output with input: 2009 'ABC321'
Year: 2009, VIN: ABC321
'''

class CarRecord:
    def __init__(self):
        self.year_made = 0
        self.car_vin = ''

    def __str__(self):
        return f'Year: {self.year_made}, VIN: {self.car_vin}'

my_car = CarRecord()
my_car.year_made = int(input())
my_car.car_vin = input()

print(my_car)