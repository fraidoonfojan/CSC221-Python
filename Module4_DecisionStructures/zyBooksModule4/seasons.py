'''
Created on Oct 16, 2024

@author: fraidoon
'''

'''
Write a program that takes a date as input and outputs the date's season in the northern hemisphere. 
The input is a string to represent the month and an int to represent the day.

'''


# Function to determine the season based on month and day
def get_season(month, day):
    # Define the ranges for seasons based on the northern hemisphere dates
    if month == "March" and day >= 20 or month == "April" or month == "May" or (month == "June" and day <= 20):
        return "Spring"
    elif month == "June" and day >= 21 or month == "July" or month == "August" or (month == "September" and day <= 21):
        return "Summer"
    elif month == "September" and day >= 22 or month == "October" or month == "November" or (month == "December" and day <= 20):
        return "Autumn"
    elif month == "December" and day >= 21 or month == "January" or month == "February" or (month == "March" and day <= 19):
        return "Winter"
    else:
        return None

# Validating input
def is_valid_date(month, day):
    # List of months with their corresponding max days
    months_with_days = {
        "January": 31, "February": 29, "March": 31, "April": 30, "May": 31, "June": 30,
        "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31
    }
    
    # Check if the month is valid and day is in the valid range for that month
    if month in months_with_days and 1 <= day <= months_with_days[month]:
        return True
    else:
        return False

# Input month and day
input_month = input()
input_day = int(input())

# Check if the date is valid
if is_valid_date(input_month, input_day):
    # Get the season based on the valid date
    season = get_season(input_month, input_day)
    print(season)
else:
    print("Invalid")