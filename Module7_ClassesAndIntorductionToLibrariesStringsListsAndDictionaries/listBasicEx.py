'''
Created on Nov 19, 2024

@author: fraidoon
'''
m = int(input())
cashier_line = input().split()

if m == 1:
    suffix = 'st'
elif m == 2:
    suffix = 'nd'
elif m == 3:
    suffix = 'rd'
else:
    suffix = 'th'

print(f'The {m}{suffix} customer is {cashier_line[m-1]}.')