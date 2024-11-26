'''
Created on Oct 8, 2024

@author: fraidoon
'''
#lists are mutable

myLottery = [22, 11, 44, 6, 3, 9, 66, 70]
print(myLottery)
myLottery.append(100)
print(myLottery)
myLottery[0]= 5
print(myLottery)
myLottery.remove(100)
print(myLottery)
myLottery.pop(1)
print(myLottery)
myLottery.sort()
print(myLottery)