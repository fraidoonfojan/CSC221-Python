'''
Created on Oct 7, 2024

@author: fraidoon
'''
'''
List countries_list is created with the first three countries read from input. 
Remove countries 'Spain' and 'Vietnam' from countries_list.
Then, read an additional two countries from input and append the two countries to countries_list, respectively.
'''

# Reads three values from input into countries_list
countries_list = [input(), input(), input()]

countries_list.remove("Spain")
countries_list.remove("Vietnam")
countries_list.append(input())
countries_list.append(input())

print(countries_list)