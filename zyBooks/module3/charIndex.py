'''
Created on Oct 2, 2024

@author: fraidoon
'''
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(alphabet[0], alphabet[2], alphabet[9])

user_number = int(input("Enter number to use as index: '"))

print("\nThe letter at index", user_number, "of the alphabet is", alphabet[user_number])

'''
Assign my_var with the last character in my_str. use a negative index
'''
my_str = 'this is just an example'
my_var = my_str[-1]
print(my_var)