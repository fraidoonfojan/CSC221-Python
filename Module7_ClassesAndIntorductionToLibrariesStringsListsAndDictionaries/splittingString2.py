'''
Created on Nov 19, 2024

@author: fraidoon
'''
'''
String color_names and integer change_at are read from input. Perform the following tasks:

Split color_names into tokens using a semicolon (";") as the separator and assign color_list with the result.
Replace the element at index change_at in color_list with "cyan".
Click here for example
Ex: If the input is:
blue;brown;brick;aqua
3
then the output is:

['blue', 'brown', 'brick', 'cyan']

'''

color_names = input()  # Read the string of color names
change_at = int(input())  # Read the integer index

# Split color_names into a list using ";" as the separator
color_list = color_names.split(";")

# Replace the element at index change_at with "cyan" if the index is valid
if 0 <= change_at < len(color_list):
    color_list[change_at] = "cyan"

# Print the resulting list
print(color_list)