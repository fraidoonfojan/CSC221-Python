'''
Created on Nov 6, 2024

@author: fraidoon
'''
'''

Complete the function definition to return the hours given minutes.

Sample output with input: 210.0
3.5
'''

def get_minutes_as_hours(orig_minutes):
    # Convert minutes to hours
    return orig_minutes / 60

# Read input and print the result
minutes = float(input())
print(get_minutes_as_hours(minutes))