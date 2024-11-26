'''
Created on Nov 19, 2024

@author: fraidoon
'''
'''

Lists waiting_to_board and on_board_bus are read from input, 
representing passengers waiting to board a bus and passengers on the bus, respectively. Perform the following tasks:

Remove the first element from waiting_to_board and output 'Passenger left bus stop: ' followed by the element.
Add all the remaining elements of waiting_to_board to the end of on_board_bus.
'''

waiting_to_board = input().split()
on_board_bus = input().split()

print(f'Passengers waiting at a bus stop: {waiting_to_board}')
print(f'Passengers on board: {on_board_bus}')

# Remove the first element from waiting_to_board
passenger_left = waiting_to_board.pop(0)

# Output the passenger who left the bus stop
print(f'Passenger left bus stop: {passenger_left}')

# Add the remaining passengers from waiting_to_board to on_board_bus
on_board_bus.extend(waiting_to_board)

# Output the updated list of passengers on board
print(f'Updated passengers on board: {on_board_bus}')