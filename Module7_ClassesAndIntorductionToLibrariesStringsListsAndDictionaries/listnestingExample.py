'''
Created on Nov 19, 2024

@author: fraidoon
'''
'''

Integer grid_size is read from input, representing the number of rows and columns 
of a two-dimensional list. 
Two-dimensional list pattern_grid is created with colons, ':', 
as the initial values. For each element at row index j and column 
index k of pattern_grid, if the sum of j and k is even, assign the 
element with 'X'.

Click here for example
Note: (j + k) % 2 == 0 returns True if j + k is even.
'''

grid_size = int(input())

# Create the initial pattern_grid with ':' values
pattern_grid = []
for j in range(grid_size):
    row = []
    for k in range(grid_size):
        row.append(':')
    pattern_grid.append(row)

# Update pattern_grid to replace ':' with 'X' where (j + k) is even
for j in range(grid_size):
    for k in range(grid_size):
        if (j + k) % 2 == 0:
            pattern_grid[j][k] = 'X'

# Print the pattern_grid row by row
for row in pattern_grid:
    for cell in row:
        print(cell, end='')
    print()