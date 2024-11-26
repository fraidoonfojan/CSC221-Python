'''
Created on Nov 6, 2024

@author: fraidoon
'''
'''
Define a function named swap_values that takes four integers as parameters and swaps the first with the second, and the third with the fourth values. Then write a main program that reads four integers from input, calls function swap_values() to swap the values, and prints the swapped values on a single line separated with spaces.


'''

def swap_values(user_val1, user_val2, user_val3, user_val4):
    # Swap the first with the second, and the third with the fourth values
    return user_val2, user_val1, user_val4, user_val3

if __name__ == '__main__':
    # Read four integers from input
    val1 = int(input())
    val2 = int(input())
    val3 = int(input())
    val4 = int(input())

    # Call swap_values() and get the swapped results
    swapped_val1, swapped_val2, swapped_val3, swapped_val4 = swap_values(val1, val2, val3, val4)
    
    # Print the swapped values on a single line
    print(swapped_val1, swapped_val2, swapped_val3, swapped_val4)