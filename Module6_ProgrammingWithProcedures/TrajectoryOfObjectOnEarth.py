'''
Created on Nov 6, 2024

@author: fraidoon
'''
'''
Common physics equations determine the x and y coordinates of a projectile object at any time, given the object's initial velocity and angle at time 0 with the initial position of x = 0 and y = 0. The equation for x is v * t * cos(a). The equation for y is v * t * sin(a) - 0.5 * g * t * t.

The program's code asks the user for the object's initial velocity, angle, and height (y position), and prints the object's position for every second until the object's y position is no longer greater than 0 (meaning the object fell back to Earth).

'''


import math

def trajectory(t, a, v, g, h): 
    """Calculates new x,y position""" 
    x = v * t * math.cos(a) 
    y = h + v * t * math.sin(a) - 0.5 * g * t * t 
    return (x,y)

def degree_to_radians(degrees): 
    """Converts degrees to radians""" 
    return ((degrees * math.pi) / 180.0)

gravity = 9.81 # Earth gravity (m/s^2) 
time = 1.0 # time (s) 
x_loc = 0 
h = 0 

angle = float(input('Launch angle (deg): ')) 
print(angle) 
angle = degree_to_radians(angle)

velocity = float(input('Launch velocity (m/s): ')) 
print(velocity)

height = float(input('Initial height (m): '))  
y_loc = height 
print(y_loc)

while ( y_loc >= 0.0 ): # While above ground 
    print(f'Time {time:3.0f} x = {x_loc:3.0f} y = {y_loc:3.0f}')
    x_loc, y_loc = trajectory(time, angle, velocity, gravity, height)  
    time += 1.0
 