'''
Created on Oct 29, 2024

@author: fraidoon
'''
'''
Requirements Analysis (English Description)
Create a program that allows a user to enter the name of each
student in a class and their final percentage in that class.
The class only has four students in it. The program should
figure out which student has the highest percentage in the
class. The program should print the name and the percentage
of the student who has the highest percentage. The program
should also print the class average.
'''

# Initialize variables
students = []
percentages = []

# Collect data for four students
for i in range(4):
    name = input(f"Enter the name of student {i + 1}: ")
    percentage = float(input(f"Enter the final percentage for {name}: "))
    
    # Store the student's name and percentage
    students.append(name)
    percentages.append(percentage)

# Calculate the student with the highest percentage
max_percentage = max(percentages)
max_index = percentages.index(max_percentage)
top_student = students[max_index]

# Calculate the class average
average_percentage = sum(percentages) / len(percentages)

# Output results
print(f"The student with the highest percentage is {top_student} with {max_percentage:.2f}%")
print(f"The class average is {average_percentage:.2f}%")