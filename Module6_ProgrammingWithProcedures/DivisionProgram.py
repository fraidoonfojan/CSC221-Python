'''
Created on Nov 5, 2024

@author: fraidoon
'''
'''
Python Program with Functions

DivisionProgram

Requirements Analysis (English Description)
Create a  program that divides one number by another number. 
These numbers should allow decimal values. This program will
use the following functions.

getNumerator
This function will ask the user for the numerator. The numerator
should be returned.

getDenominator
This function will ask the user for the denominator. If the
denominator is equal to 0, the program should print an error
message and ask the user for the denominator again. This 
function should continue to ask the user for the denominator
as long as the denominator is equal to 0. Once the user
enters a number other than 0, the denominator should be
returned.

calculateQuotient
This function will calculate the quotient by dividing the 
numerator by the denominator. The quotient  should be
returned

printQuotient
This function will print the numerator, the denominator,
and the quotient

Design (Algorithm)

Implementation
'''

def getNumerator():
    # Ask the user for the numerator and return it as a float
    numerator = float(input("Enter the numerator: "))
    return numerator

def getDenominator():
    # Continuously ask for the denominator until a non-zero value is entered
    while True:
        denominator = float(input("Enter the denominator (non-zero): "))
        if denominator != 0:
            return denominator
        else:
            print("Error: Denominator cannot be zero. Please enter a non-zero value.")

def calculateQuotient(numerator, denominator):
    # Calculate and return the quotient
    quotient = numerator / denominator
    return quotient

def printQuotient(numerator, denominator, quotient):
    # Print the numerator, denominator, and the calculated quotient
    print(f"Numerator: {numerator}")
    print(f"Denominator: {denominator}")
    print(f"Quotient: {quotient}")

# Main Program
numerator = getNumerator()
denominator = getDenominator()
quotient = calculateQuotient(numerator, denominator)
printQuotient(numerator, denominator, quotient)