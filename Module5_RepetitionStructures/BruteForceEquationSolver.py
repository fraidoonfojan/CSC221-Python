'''
Created on Oct 29, 2024

@author: fraidoon
'''
'''
Numerous engineering and scientific applications require finding solutions to a set of equations. Ex: 8x + 7y = 38 and 3x - 5y = -1 have a solution x = 3, y = 2. Given integer coefficients of two linear equations with variables x and y, use brute force to find an integer solution for x and y in the range -10 to 10.

'''
# Read the coefficients and constants from input
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

# Initialize a flag to indicate if a solution is found
solution_found = False

# Brute-force search for integer solutions of x and y in the range -10 to 10
for x in range(-10, 11):
    for y in range(-10, 11):
        # Check if (x, y) satisfies both equations
        if (a * x + b * y == c) and (d * x + e * y == f):
            print(f"x = {x}, y = {y}")
            solution_found = True
            break  # Exit the inner loop if a solution is found
    if solution_found:
        break  # Exit the outer loop if a solution is found

# If no solution is found, print "No solution"
if not solution_found:
    print("No solution")