'''
Created on Oct 7, 2024

@author: fraidoon
'''

print("what you wanna buy?")
item = input()
print("what is the price of the item?")
cost = float(input())

tax = 0.06 * cost
totalAmount = cost + tax

print("the tax paid on this item is $", f'{tax:.2f}')
print("the total cost of this item is $", f"{totalAmount:.2f}")
           

        