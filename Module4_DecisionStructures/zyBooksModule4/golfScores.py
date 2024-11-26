'''
Created on Oct 16, 2024

@author: fraidoon
'''
'''
Golf scores record the number of strokes used to get the ball in the hole. The expected number of strokes varies from hole to hole and is called par (possible values: 3, 4, or 5). Each score's name is based on the actual strokes taken compared to par:

"Eagle": number of strokes is two less than par
"Birdie": number of strokes is one less than par
"Par": number of strokes equals par
"Bogey": number of strokes is one more than par
Given two integers that represent the number of strokes used and par, write a program that prints the appropriate score name. Print "Error" at the end of the output if par is not 3, 4, or 5, or if the score's name is not "Eagle", "Birdie", "Par", or "Bogey".

'''
# Input the number of strokes and the par value
strokes = int(input())
par = int(input())

# Check if the par value is valid (3, 4, or 5)
if par not in [3, 4, 5]:
    print(f"Par {par} in {strokes} strokes is Error")
else:
    # Determine the golf score name based on strokes and par
    if strokes == par - 2:
        score_name = "Eagle"
    elif strokes == par - 1:
        score_name = "Birdie"
    elif strokes == par:
        score_name = "Par"
    elif strokes == par + 1:
        score_name = "Bogey"
    else:
        score_name = "Error"
    
    # Output the result
    print(f"Par {par} in {strokes} strokes is {score_name}")