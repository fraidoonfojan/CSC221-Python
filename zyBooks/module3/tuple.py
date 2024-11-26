'''
Created on Oct 7, 2024

@author: fraidoon
'''
white_house_coordinates = (38.8977, 77.0366)
print(f'Coordinates: {white_house_coordinates}')
print(f'Tuple length: {len(white_house_coordinates)}')

# Access tuples via index
print(f'\nLatitude: {white_house_coordinates[0]} north')
print(f'Longitude: {white_house_coordinates[1]} west\n')

# Error. Tuples are immutable
#white_house_coordinates[1] = 50

#Create a new variable point that is a tuple containing the strings 'X string' and 'Y string'.
point = ("X string", "Y string")
print(point)