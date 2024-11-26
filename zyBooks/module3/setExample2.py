'''
Created on Oct 7, 2024

@author: fraidoon
'''
colors_chosen = {'cyan', 'indigo'}

new_color = input()
colors_chosen.add(new_color)
num_colors = len(colors_chosen)


print(sorted(colors_chosen))
print(f'Number of values chosen: {num_colors}')