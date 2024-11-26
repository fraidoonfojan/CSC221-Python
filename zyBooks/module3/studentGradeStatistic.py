'''
Created on Oct 7, 2024

@author: fraidoon
'''

#Program to calculate statistics from student test scores.
midterm_scores = [84, 58, 99, 97, 79, 81, 76, 87, 88, 97]
final_scores = [78, 88, 58, 94, 76, 77]

#Combine the scores into a single list
all_scores = midterm_scores + final_scores

num_midterm_scores = len(midterm_scores)
num_final_scores = len(final_scores)

print(f"{num_midterm_scores} students took midterm.")
print(f"{num_final_scores} students took the final.")

#Calculate the number of students who took the midterm but not the final
dropped_students = num_midterm_scores - num_final_scores
print(f" {dropped_students} students must have dropped class")

lowest_final = min(final_scores)
highest_final = max(final_scores)
print(f"final scores ranged from {lowest_final} to {highest_final}")

# Calculate the average midterm and final scores
avg_midterm = sum(midterm_scores) / len(midterm_scores)
print(f"the average scores for midterm {avg_midterm:.2f}")

avg_final = sum(final_scores) / num_final_scores
print(f"the average final is: {avg_final:.2f}")
