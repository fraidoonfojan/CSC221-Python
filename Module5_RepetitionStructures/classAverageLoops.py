'''
Created on Oct 21, 2024

@author: fraidoon
'''
'''
ClassAverage

Requirements Analysis (English Description)
Create a program that allows a user to enter the names
and the scores of the students who took a final exam.
The program will ask the user for the name of the 
students and the scores the student received on their
final exam. If the score entered by the user is not 
between 0 and 100, then an error message should be
given to the user. If the score is between 0 and 100,
then that score will be added to the total score. When
the user is done entering the scores of the students,
they should enter the word 'done' for the name of the 
next student. After all scores have been entered, the
class average should be displayed (2 decimal points)
to the screen.
'''
# Initialize variables
total_score = 0
student_count = 0

while True:
    # Get the student's name
    student_name = input("Enter the student's name (or 'done' to finish): ")

    # Check if the user is done entering students
    if student_name.lower() == 'done':
        break

    # Get the student's score
    try:
        score = float(input(f"Enter {student_name}'s score (0-100): "))

        # Check if the score is valid
        if 0 <= score <= 100:
            total_score += score  # Add the score to the total
            student_count += 1  # Increment the student count
        else:
            print("Error: Score must be between 0 and 100.")
    
    except ValueError:
        print("Error: Please enter a valid numeric score.")

# Calculate and display the class average, if there are students
if student_count > 0:
    class_average = total_score / student_count
    print(f"Class average: {class_average:.2f}")
else:
    print("No scores were entered.")