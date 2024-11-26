'''
Created on Oct 9, 2024

@author: fraidoon

'''
'''
Given the user inputs, complete a program that does the following tasks:

Define a list, my_list, containing the user inputs: my_flower1, my_flower2, and my_flower3 in the same order.
Define a list, your_list, containing the user inputs, your_flower1 and your_flower2, in the same order.
Define a list, our_list, by concatenating my_list and your_list.
Append the user input, their_flower, to the end of our_list.
Replace my_flower2 in our_list with their_flower.
Remove the first occurrence of their_flower from our_list without using index().
Remove the second element of our_list.
'''

# Input: Read user inputs for the flowers
my_flower1 = input()
my_flower2 = input()
my_flower3 = input()

your_flower1 = input()
your_flower2 = input()

their_flower = input()

# 1. Define my_list containing my_flower1, my_flower2, and my_flower3 in that order
my_list = [my_flower1, my_flower2, my_flower3]

# 2. Define your_list containing your_flower1 and your_flower2 in that order
your_list = [your_flower1, your_flower2]

# 3. Define our_list by concatenating my_list and your_list
our_list = my_list + your_list
print(our_list)  # Output after concatenation

# 4. Append their_flower to the end of our_list
our_list.append(their_flower)
print(our_list)  # Output after appending their_flower

# 5. Replace my_flower2 in our_list with their_flower
our_list[our_list.index(my_flower2)] = their_flower
print(our_list)  # Output after replacing my_flower2 with their_flower

# 6. Remove the first occurrence of their_flower from our_list without using index()
our_list.remove(their_flower)
print(our_list)  # Output after removing the first occurrence of their_flower

# 7. Remove the second element of our_list
del our_list[1]
print(our_list)  # Output after removing the second element