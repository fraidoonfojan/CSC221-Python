'''
Created on Oct 7, 2024

@author: fraidoon
'''
#Create variable unique_colors as an empty set so that four strings can be read from input and added to unique_colors.

unique_colors = set()

color1 = input()
color2 = input()
color3 = input()
color4 = input()

unique_colors.add(color1)
unique_colors.add(color2)
unique_colors.add(color3)
unique_colors.add(color4)

print(sorted(unique_colors))