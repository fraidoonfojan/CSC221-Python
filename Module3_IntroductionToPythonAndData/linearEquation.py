'''
Created on Oct 7, 2024

@author: fraidoon

'''
from _ast import In
'''Program Name: Linear Equation

Requirements Analysis:

Create a program that calculates the y value of a linear equation given the slope (m),

the x value, and the y-intercept (b) in the following equation: y=mx+b.

The user will enter the values of the slope, the x value, and the y-intercept.

The program will then determine the value of y using the equation.

This program should display the computed value of y'''

print("This program computes the y value of a linear equation given the slope (m), the x value," )

print("and the y-intercept (b) in the following equation: y=mx+b.\n ")

print("Enter slope m: ")
slope = float(input())
print("Enter the x value: ")
xValue = int(input())
print("Enter y intercept b: ")
yIntercept = int(input())

yValue = slope * xValue + yIntercept
print("Y value = ", yValue)