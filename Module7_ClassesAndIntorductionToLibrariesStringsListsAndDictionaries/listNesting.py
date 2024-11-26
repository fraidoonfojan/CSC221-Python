'''
Created on Nov 19, 2024

@author: fraidoon
'''
'''
List nesting
Since a list can contain any type of object as an element, and 
a list is itself an object, a list can contain another 
list as an element. Such embedding of a list inside another 
list is known as list nesting. 
Ex: The code my_list = [[5, 13], [50, 75, 100]] creates a list with 
two elements that are each another list.


Example: Two-dimensional list tictactoe represents
 a 3x3 tic-tac-toe game board read from input. List tictactoe 
 contains three lists, each representing a row. 
 Each list has three elements representing the three columns on the board. 
 Each element in the tic-tac-toe game board is 'x', 'o', or '-'.

If all the elements at column index 0 are 'x', output 'A win at column 0.' 
Otherwise, output 'No win at column 0.'
'''

tictactoe = [
    input().split(),
    input().split(),
    input().split()
]

# Check if all elements in column 0 are 'x'
if tictactoe[0][0] == 'x' and tictactoe[1][0] == 'x' and tictactoe[2][0] == 'x':
    print('A win at column 0.')
else:
    print('No win at column 0.')