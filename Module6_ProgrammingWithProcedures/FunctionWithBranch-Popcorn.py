'''
Created on Nov 5, 2024

@author: fraidoon
'''
'''
Define function print_popcorn_time() with parameter bag_ounces. If bag_ounces is less than 3, print "Too small". If greater than 10, print "Too large". Otherwise, compute and print 6 * bag_ounces followed by " seconds".

'''

def print_popcorn_time(bag_ounces):
    if bag_ounces < 3:
        print("Too small")
    elif bag_ounces > 10:
        print("Too large")
    else:
        print(f"{6 * bag_ounces} seconds")

# Get user input for bag_ounces and call the function
bag_ounces = int(input())
print_popcorn_time(bag_ounces)