'''
Created on Nov 21, 2024

@author: fraidoon
'''
'''
Mad Libs are activities that have a person provide various 
words, which are then used to complete a short story in 
unexpected (and hopefully funny) ways.

Write a program that takes a string and an integer as input, 
and outputs a sentence using the input values as shown in 
the example below. The program repeats until the input string is 
quit and disregards the integer input that follows.

Ex: If the input is:

apples 5
shoes 2
quit 0
the output is:

Eating 5 apples a day keeps you happy and healthy.
Eating 2 shoes a day keeps you happy and healthy.

'''

while True:
    user_input = input()
    word, number = user_input.split()  # Split the input into a word and a number
    if word == "quit":  # Check if the word is "quit"
        break
    number = int(number)  # Convert the number part to an integer
    print(f"Eating {number} {word} a day keeps you happy and healthy.")