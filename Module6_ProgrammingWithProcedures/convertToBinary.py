'''
Created on Nov 6, 2024

@author: fraidoon
'''
def int_to_reverse_binary(integer_value):
    binary_str = ''
    while integer_value > 0:
        binary_str += str(integer_value % 2)
        integer_value = integer_value // 2
    return binary_str

def string_reverse(input_string):
    return input_string[::-1]

if __name__ == '__main__':
    # Read an integer input
    integer_value = int(input())
    
    # Get the reversed binary string
    reversed_binary = int_to_reverse_binary(integer_value)
    
    # Reverse the reversed binary string to get the correct binary
    binary_result = string_reverse(reversed_binary)
    
    # Output the result
    print(binary_result)