'''
Created on Oct 16, 2024

@author: fraidoon
'''
silver_temp = int(input())

if silver_temp <= 1760:
    print("The silver is now a solid.")
elif 1760 < silver_temp < 3939:
    print('The silver is now a liquid.')
else:
    print('The silver is now a gas.')
        