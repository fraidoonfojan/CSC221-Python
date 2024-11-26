'''
Created on Oct 29, 2024

@author: fraidoon
'''
'''

Calculate quotient
Requirements Analysis (English Description)
Create a program that allows a user to divide one number by another number. The program
should ask the user for the numerator. The program should then ask the user for the
denominator. The user will continue to be asked for a denominator as long as they
keep entering 0 as the denominator. Once the user enters a value other than 0 for the 
denominator, the program should calculate the quotient and display it to the screen.
The program should allow the user to enter decimal values for the numerator and the
denominator and should display the quotient as a decimal value. The program should
continue as long as the user would like to calculate quotients.

'''
print("This program allows you to divide one number by another.")
continue_calculating = 'y'

# Loop to allow multiple calculations
while continue_calculating.lower() == 'y':
    # Ask the user for the numerator
    numerator = float(input("Enter the numerator: "))

    # Ask the user for the denominator, ensuring it is not zero
    denominator = 0
    while denominator == 0:
        denominator = float(input("Enter the denominator (cannot be 0): "))
        if denominator == 0:
            print("Denominator cannot be zero. Please enter a different value.")

    # Calculate and display the quotient
    quotient = numerator / denominator
    print(f"The quotient is: {quotient:.2f}")

    # Ask the user if they want to continue
    continue_calculating = input("Would you like to calculate another quotient? (y/n): ")

print("Thank you for using the division calculator.")