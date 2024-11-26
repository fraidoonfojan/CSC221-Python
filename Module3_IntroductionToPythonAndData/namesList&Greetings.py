'''
Created on Oct 8, 2024

@author: fraidoon
'''
#Program Name: NamesAndGreetings
from ntpath import sep
from _testcapi import MyList

#Requirements Analysis (English Description)
#Create a program that stores the names of a few of your
#friends in a list called names. Print a message to each
#of your friends. The text of each message should be the
#same, but each message should be personalized with the
#person's name.

#Design (Algorithm)

#Implementation

#Test

my_frieds_list = ["aman", "jaman", "kaman", "ghaman", "talan"]
messge = "I am glad you are my friend"
print("I have", len(my_frieds_list),"friends")
print(my_frieds_list[0], messge, sep = ', ')
print(my_frieds_list[1], messge, sep = ', ')
print(my_frieds_list[2], messge, sep = ', ')
print(my_frieds_list[3], messge, sep = ', ')
print(my_frieds_list[4], messge, sep = ', ')

print(max(my_frieds_list))
print(min(my_frieds_list))

myList = []
name1 = input("Name 1 ")
myList.append(name1)
name2 = input("Name 2 ")
myList.append(name2)
name3 = input("Name 3 ")
myList.append(name3)
name4 = input("Name 4 ")
myList.append(name4)
name5 = input("Name 5 ")
myList.append(name5)

print(myList[0], messge, sep=' ')
print(myList[1], messge, sep=' ')
print(myList[2], messge, sep=' ')
print(myList[3], messge, sep=' ')
print(myList[4], messge, sep=' ')

myList.insert(1, "Pashan")
print(myList)
print(len(myList))