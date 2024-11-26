'''
Created on Oct 9, 2024

@author: fraidoon
'''
'''
Dictionary room_guest_pairs contains four key-value pairs, each representing a hotel room number and the guest's name. Read a room number from input. Then, output the corresponding guest's name from room_guest_pairs. Finally, delete that pair from room_guest_pairs. 

'''

# Given dictionary with room number and guest pairs
room_guest_pairs = {758: 'Val', 273: 'Aya', 334: 'Abe', 339: 'Noa'}

# Input: Read the room number
room_number = int(input())

# Output the guest's name for the corresponding room number
print(room_guest_pairs[room_number])

# Delete the pair corresponding to the input room number
del room_guest_pairs[room_number]

# Output the remaining pairs
print('Remaining pairs:')
print(room_guest_pairs)