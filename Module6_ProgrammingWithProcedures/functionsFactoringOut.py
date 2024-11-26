'''
Created on Nov 5, 2024

@author: fraidoon
'''
'''
Write a function so that the main program below can be replaced by the simpler code that calls function mph_and_minutes_to_miles(). Original main program:
miles_per_hour = float(input())
minutes_traveled = float(input())
hours_traveled = minutes_traveled / 60.0
miles_traveled = hours_traveled * miles_per_hour

print(f'Miles: {miles_traveled:f}')


Sample output with inputs: 70.0 100.0
Miles: 116.666667


'''
def mph_and_minutes_to_miles(mph, minutes):
    hours_traveled = minutes / 60.0
    miles_traveled = hours_traveled * mph
    return miles_traveled

miles_per_hour = float(input())
minutes_traveled = float(input())

print(f'Miles: {mph_and_minutes_to_miles(miles_per_hour, minutes_traveled):f}')