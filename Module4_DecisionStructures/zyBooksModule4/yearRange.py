'''
Created on Oct 16, 2024

@author: fraidoon
'''
'''
If input_year is in the inclusive range:

501 - 600, output 'The 6th century'.
601 - 700, output 'The 7th century'.
701 - 800, output 'The 8th century'.
Otherwise, output 'Not in the period of research'.
'''

input_year = int(input())  # Read input year as an integer

# Check which century the input year belongs to
if 501 <= input_year <= 600:
    print("The 6th century")
elif 601 <= input_year <= 700:
    print("The 7th century")
elif 701 <= input_year <= 800:
    print("The 8th century")
else:
    print("Not in the period of research")