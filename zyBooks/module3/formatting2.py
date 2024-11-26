'''
Created on Oct 9, 2024

@author: fraidoon
'''
'''
x and y are read from input as floating-point values, representing the base and height of a triangle. Compute the triangle's area as (x*y)/2. Use f-string's = sign feature within the provided curly brackets as the replacement field to output both the expression and result.

'''
x = float(input())
y = float(input())

print(f'{(x*y)/2=}')