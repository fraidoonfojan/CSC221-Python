'''
Created on Oct 16, 2024

@author: fraidoon
'''
'''
Write a program with total change amount as an integer input, 
and output the change using the fewest coins, one coin type per line. The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.
'''
# Input the total change amount
total_change = int(input())

if total_change <= 0:
    print("No change")
else:
    # Calculate the number of dollars
    dollars = total_change // 100
    total_change %= 100  # Remaining change after dollars

    # Calculate the number of quarters
    quarters = total_change // 25
    total_change %= 25  # Remaining change after quarters

    # Calculate the number of dimes
    dimes = total_change // 10
    total_change %= 10  # Remaining change after dimes

    # Calculate the number of nickels
    nickels = total_change // 5
    total_change %= 5  # Remaining change after nickels

    # Remaining change is the number of pennies
    pennies = total_change

    # Output the result, using singular and plural forms as necessary
    if dollars > 0:
        if dollars == 1:
            print("1 Dollar")
        else:
            print(f"{dollars} Dollars")

    if quarters > 0:
        if quarters == 1:
            print("1 Quarter")
        else:
            print(f"{quarters} Quarters")

    if dimes > 0:
        if dimes == 1:
            print("1 Dime")
        else:
            print(f"{dimes} Dimes")

    if nickels > 0:
        if nickels == 1:
            print("1 Nickel")
        else:
            print(f"{nickels} Nickels")

    if pennies > 0:
        if pennies == 1:
            print("1 Penny")
        else:
            print(f"{pennies} Pennies")