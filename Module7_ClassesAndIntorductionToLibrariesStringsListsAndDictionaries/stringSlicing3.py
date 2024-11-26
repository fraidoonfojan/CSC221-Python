'''
Created on Nov 19, 2024

@author: fraidoon
'''
'''
String my_string is read from input. Assign variable sub_string with the my_string slice that excludes the character at index 9.

'''

my_string = input()

sub_string = my_string[:9] + my_string[10:]

print(sub_string)