'''
Created on Oct 30, 2024

@author: fraidoon
'''
'''

List color_popularities contains four colors read from input. Complete the for loop using the enumerate() function to output each color's popularity ranking followed by the color.

'''

color_popularities = [input(), input(), input(), input()]

for (idx, color) in  enumerate(color_popularities):
    print(f'#{idx + 1}: {color}')