'''
Created on Oct 7, 2024

@author: fraidoon
'''
#Set my_favorites contains 'Del', 'Kai', and 'Pat'. Set your_favorites contains three strings read from input. Assign our_favorites with the intersection of my_favorites and your_favorites.
my_favorites = {'Del', 'Kai', 'Pat'}
your_favorites = {input(), input(), input()}

our_favorites = my_favorites.intersection(your_favorites)

print(f'My favorite names: {sorted(my_favorites)}')
print(f'Your favorite names: {sorted(your_favorites)}')
print(f'Our favorite names: {sorted(our_favorites)}')