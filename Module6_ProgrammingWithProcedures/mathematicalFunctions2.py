'''
Created on Nov 5, 2024

@author: fraidoon
'''

def find_base_area(base_length, base_width):
    return base_length * base_width

def find_vol(base_length, base_width, height):
    base_area = find_base_area(base_length, base_width)
    return (base_area * height) / 3

user_base_length = float(input())
user_base_width = float(input())
user_height = float(input())

print(f'Base length: {user_base_length}')
print(f'Base width: {user_base_width}')
print(f'Height: {user_height}')
print(f'Base area: {find_base_area(user_base_length, user_base_width):.1f}')
print(f'Volume: {find_vol(user_base_length, user_base_width, user_height):.1f}')