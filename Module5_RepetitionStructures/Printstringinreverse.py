'''
Created on Oct 29, 2024

@author: fraidoon
'''
'''
Print string in reverse: Write a program that takes in a line of text as input, and outputs that line of text in reverse. The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.

'''

while True:
    # Take a line of text as input
    text = input("Enter a line of text (or 'Done', 'done', 'd' to quit): ")
    
    # Check if the input is a stop word
    if text in ["Done", "done", "d"]:
        break  # Exit the loop if stop word is entered
    
    # Output the reversed text
    print(text[::-1])
