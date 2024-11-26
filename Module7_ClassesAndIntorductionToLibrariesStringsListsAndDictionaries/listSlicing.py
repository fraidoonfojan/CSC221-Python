'''
Created on Nov 19, 2024

@author: fraidoon
'''
'''
A programmer can use slice notation to read multiple elements from a list, 
creating a new list that contains only the desired elements. 
The programmer indicates the start and end positions of a range of 
elements to retrieve, as in my_list[0:2]. The 0 is the position of 
the first element to read, and the 2 indicates the last element. 
Every element between 0 and 2 from my_list is in the new list. 
The end position, 2, is not included in the resulting list.


Example:List food_list is read from input. 
Assign selected_items with a slice of food_list 
from the third element up to and excluding the last element.
'''

food_list = input().split()

selected_items = food_list[2:-1]

print(f'Original food items: {food_list}')
print(f'Selected food items: {selected_items}')