'''
Created on Nov 21, 2024

@author: fraidoon
'''
'''
Write a program whose input is a string which contains a character 
and a phrase, and whose output indicates the number of times 
the character appears in the phrase. The output should include 
the input character and use the plural form, n's, if the 
number of times the characters appears is not exactly 1.

Ex: If the input is:

n Monday
the output is:

1 n
Ex: If the input is:

z Today is Monday
the output is:

0 z's
Ex: If the input is:

n It's a sunny day
the output is:

2 n's
Case matters. n is different than N.

Ex: If the input is:

n Nobody
the output is:

0 n's

'''
user_input = input()
char_to_count = user_input[0]  # First character is the one to count
phrase = user_input[2:]  # Rest of the string is the phrase

count = phrase.count(char_to_count)  # Count occurrences of the character

# Determine the correct output format based on count
if count == 1:
    print(f"{count} {char_to_count}")
else:
    print(f"{count} {char_to_count}'s")
