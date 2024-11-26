'''
Created on Oct 8, 2024

@author: fraidoon
'''
from zyBooks.module3.concatinatingList import house_prices
houseFairfax = [250000, 300000, 150000, 640000, 780000]
houseAlexandria = [650000, 410000, 320000, 390000]

housePrices = houseFairfax + houseAlexandria
print("there are", len(housePrices), "prices in the list")
print(housePrices)

#find min, max

print("Cheapest house is: $", min(house_prices))
print("The most expensive house is: $", max(house_prices))
print("The total price for the houses is: $", sum(house_prices))