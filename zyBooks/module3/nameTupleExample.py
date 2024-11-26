'''
Created on Oct 7, 2024

@author: fraidoon
'''
from collections import namedtuple

Person = namedtuple('Person', ['first_name', 'last_name', 'birthday'])

person_data = Person(input(), input(), input())

print(f"First name: {person_data.first_name}")
print(f"Last name: {person_data.last_name}")
print(f"Birthday: {person_data.birthday}")