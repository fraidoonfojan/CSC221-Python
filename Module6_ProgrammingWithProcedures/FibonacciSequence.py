'''
Created on Nov 6, 2024

@author: fraidoon
'''
'''
The Fibonacci sequence begins with 0 and then 1 follows. All subsequent values are the sum of the previous two, ex: 0, 1, 1, 2, 3, 5, 8, 13. Complete the fibonacci() function, which has an index, n (starting at 0), as a parameter and returns the nth value in the sequence. Any negative index values should return -1.


'''

def fibonacci(n):
    if n < 0:
        return -1  # Return -1 for negative indices
    elif n == 0:
        return 0  # The first value in Fibonacci sequence
    elif n == 1:
        return 1  # The second value in Fibonacci sequence
    else:
        # Calculate Fibonacci using an iterative approach
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')