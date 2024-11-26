'''
Created on Nov 6, 2024

@author: fraidoon
'''
'''
A pedometer treats walking 1 step as walking 2.5 feet. Define a function named feet_to_steps that takes a float as a parameter, representing the number of feet walked, and returns the number of steps walked as an integer by using int(). Then, write a main program that reads the number of feet walked as an input, calls function feet_to_steps() with the input as an argument, and outputs the number of steps returned from feet_to_steps().

Use floating-point arithmetic to perform the conversion.

Note: Converting a float to an integer may affect the result's accuracy.

'''

def feet_to_steps(user_feet):
    # Convert feet to steps (1 step = 2.5 feet)
    steps = int(user_feet / 2.5)
    return steps

if __name__ == '__main__':
    # Read the number of feet walked from input
    feet_walked = float(input())
    
    # Call feet_to_steps and print the result
    print(feet_to_steps(feet_walked))