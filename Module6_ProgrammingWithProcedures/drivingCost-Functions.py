'''
Created on Nov 6, 2024

@author: fraidoon
'''
'''

Write a function driving_cost() with parameters miles_per_gallon, dollars_per_gallon, and miles_driven, that returns the dollar cost to drive those miles. All items are of type float. The function called with arguments (20.0, 3.1599, 50.0) returns 7.89975.

The main program's inputs are the car's miles per gallon and the price of gas in dollars per gallon (both float). Output the gas cost for 10 miles, 50 miles, and 400 miles, by calling your driving_cost() function three times.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')

'''
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    # Calculate the cost of driving the given miles
    cost = (miles_driven / miles_per_gallon) * dollars_per_gallon
    return cost

if __name__ == '__main__':
    # Read inputs
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())

    # Output the gas cost for 10, 50, and 400 miles
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10):.2f}')
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 50):.2f}')
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 400):.2f}')