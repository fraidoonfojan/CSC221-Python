'''
Created on Nov 21, 2024

@author: fraidoon
'''
'''
Reverse list
Complete the reverse_list() function that returns a new integer 
list containing all contents in the list parameter but in reverse order.

Ex: If the elements of the input list are:

[2, 4, 6]
the returned array will be:

[6, 4, 2]
Note: Use a for loop. DO NOT use reverse() or reversed().

'''
def reverse_list(li):
    reversed_list = []  # Initialize an empty list for reversed elements
    for i in range(len(li) - 1, -1, -1):  # Iterate from the last index to the first
        reversed_list.append(li[i])  # Append each element to the reversed list
    return reversed_list

if __name__ == '__main__':
    int_list = [2, 4, 6]
    print(reverse_list(int_list))  # Should print [6, 4, 2]