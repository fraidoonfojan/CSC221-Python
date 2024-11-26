'''
Created on Oct 7, 2024

@author: fraidoon
'''
# Concatenating lists
house_prices = [380000, 900000, 875000] + [225000]
print(f'There are {len(house_prices)} prices in the list.')

# Finding min, max
print(f'Cheapest house: {min(house_prices)}')
print(f'Most expensive house: {max(house_prices)}')