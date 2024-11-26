'''
Created on Oct 7, 2024

@author: fraidoon
'''
fav_animal1 = input()
fav_animal2 = input()

length_difference = len(fav_animal1) - len(fav_animal2)
#print(f"{fav_animal2} has {length_difference} less character(s) than {fav_animal1}")

print(fav_animal2, "has", length_difference, "less character(s) than", fav_animal1)