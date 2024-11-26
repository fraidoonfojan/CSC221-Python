'''
Created on Oct 29, 2024

@author: fraidoon
'''
'''
Variable keep_bidding is initially assigned with 'y'. Within the while loop, keep_bidding is updated with the user's next input value. Complete the while loop's expression to terminate the while loop if the user enters 'n'.

'''
import random
random.seed(5)

keep_bidding = 'y'
next_bid = 0

while keep_bidding != 'n':
   next_bid = next_bid + random.randint(1, 10)
   print(f'I\'ll bid ${next_bid}!')
   print('Continue bidding? (y/n)', end=' ')
   keep_bidding = input()