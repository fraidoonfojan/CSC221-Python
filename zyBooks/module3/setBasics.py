'''
Created on Oct 9, 2024

@author: fraidoon
'''

'''
Given the user inputs, complete a program that does the following tasks:

Define a set, fruits, containing the user inputs: my_fruit1, my_fruit2, and my_fruit3.
Add the user inputs, your_fruit1 and your_fruit2, to fruits.
Add the user input, their_fruit, to fruits.
Add your_fruit1 to fruits.
Remove my_fruit1 from fruits.
'''

# Input: Read the fruits from the user
my_fruit1 = input()
my_fruit2 = input()
my_fruit3 = input()

your_fruit1 = input()
your_fruit2 = input()

their_fruit = input()

# 1. Define a set, fruits, containing my_fruit1, my_fruit2, and my_fruit3
fruits = {my_fruit1, my_fruit2, my_fruit3}
print(sorted(fruits))  # Output the sorted set

# 2. Add your_fruit1 and your_fruit2 to fruits
fruits.add(your_fruit1)
fruits.add(your_fruit2)
print(sorted(fruits))  # Output the sorted set

# 3. Add their_fruit to fruits
fruits.add(their_fruit)
print(sorted(fruits))  # Output the sorted set

# 4. Add your_fruit1 to fruits (even though it's already there, it won't be duplicated since it's a set)
fruits.add(your_fruit1)
print(sorted(fruits))  # Output the sorted set

# 5. Remove my_fruit1 from fruits
fruits.discard(my_fruit1)  # Use discard() to avoid an error if the fruit doesn't exist
print(sorted(fruits))  # Output the sorted set