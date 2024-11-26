'''
Created on Oct 7, 2024

@author: fraidoon
'''
#Import the namedtuple container from collections. Then, define a named tuple called School with fields: name, city, state, and enrollment, in that order.

from collections import namedtuple
School = namedtuple("School",["name", "city", 'state', "enrollment"]) 

school_name = input()
city_located = input()
state_located = input()
enrollment_count = int(input())

school_info = School(school_name, city_located, state_located, enrollment_count)

print(f'School name: {school_info.name}, City: {school_info.city}, State: {school_info.state}, Enrollment: {school_info.enrollment}')