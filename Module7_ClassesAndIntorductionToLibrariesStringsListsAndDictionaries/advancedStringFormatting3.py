'''
Created on Nov 19, 2024

@author: fraidoon
'''
'''
Three strings are read from input and stored into list musicians. Then, three more strings are read from input and stored into list years_played. Lastly, string separator_char is read from input. Use five print(f' ') statements to output the following five lines:

"Musicians", with a field width of 14, centered, and followed by '|'. Then "Years Played", with a field width of 14, centered.
28 instances of separator_char.
musicians[0], with a field width of 14, left-aligned, and followed by '|'. Then, years_played[0] with a field width of 14, left-aligned.
musicians[1], with a field width of 14, left-aligned, and followed by '|'. Then, years_played[1] with a field width of 14, left-aligned.
musicians[2], with a field width of 14, left-aligned, and followed by '|'. Then, years_played[2] with a field width of 14, left-aligned.

'''


musicians = input().split()
years_played = input().split()
separator_char = input()

print(f'{"Musicians":^14}|{"Years Played":^14}')
print(separator_char * 28)
print(f'{musicians[0]:<14}|{years_played[0]:<14}')
print(f'{musicians[1]:<14}|{years_played[1]:<14}')
print(f'{musicians[2]:<14}|{years_played[2]:<14}')