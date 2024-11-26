'''
Created on Oct 3, 2024

@author: fraidoon
'''

print("please enter hourly wage")
hourlyWage  = float(input())

print("please enter hours per week")
hoursWeek = int(input())

print("please enter how many weeks the employee worked")
weeksaYear = int(input())

annualSalary = hourlyWage * hoursWeek * weeksaYear

monthlySalary = annualSalary / 12
print("monthly salary of the employee is $", monthlySalary)


print("annual salary employee gets is $", annualSalary)
print(f'{annualSalary:.2f}') #formatted with 2 decimal digits