'''
Created on Nov 19, 2024

@author: fraidoon
'''
'''

String consonants_string is read from input. If 'l' is in consonants_string, then:

Output 'Located at: ' followed by the index of the last occurrence.
Create a string from consonants_string with the first two occurrences of 'l' replaced by '+' and output consonants_string on a newline.


'''

consonants_string = input()

# Check if 'l' is in consonants_string
if 'l' in consonants_string:
    # Output the index of the last occurrence of 'l'
    print(f'Located at: {consonants_string.rfind("l")}')
    
    # Replace the first two occurrences of 'l' with '+'
    updated_string = consonants_string.replace('l', '+', 2)
    
    # Output the modified string
    print(updated_string)
else:
    # If 'l' is not found, output "No matches"
    print("No matches")