'''
Created on Oct 9, 2024

@author: fraidoon
'''
'''
Dictionary num_to_word contains multiple number and word pairs. Read integers from_time and to_time from input, representing an event's start and end times. Use num_to_word to access the corresponding word of each integer. Then, output the starting time as a word, followed by ' to ' and the ending time as a word.

'''
# Given dictionary num_to_word with number to word mappings
num_to_word = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four',
    5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
    9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve'
}

# Input: Read the starting time and ending time as integers
from_time = int(input())
to_time = int(input())

# Output the corresponding words for the start and end times
print(f'{num_to_word[from_time]} to {num_to_word[to_time]}')
