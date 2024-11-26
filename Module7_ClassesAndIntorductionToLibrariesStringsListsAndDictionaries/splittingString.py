'''
Created on Nov 19, 2024

@author: fraidoon
'''
'''

String athlete_names is read from input. Split athlete_names into tokens using the default separator and assign users_list with the result.
Ex: If the input is Ayaka Ezra Aoife, then the output is:

['Ayaka', 'Ezra', 'Aoife']
'''

athlete_names = input()

users_list = athlete_names.split()

print(users_list)