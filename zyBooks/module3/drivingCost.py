'''
Created on Oct 2, 2024

@author: fraidoon
'''
mileage = float(input())
cost_per_gallon = float(input())

cost_20_miles = (20 / mileage) * cost_per_gallon
cost_75_miles = (75 / mileage) * cost_per_gallon
cost_500_miles = (500 / mileage) * cost_per_gallon

print(f'{cost_20_miles:.2f} {cost_75_miles:.2f} {cost_500_miles:.2f}')
