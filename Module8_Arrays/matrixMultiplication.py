'''
Created on Nov 26, 2024

@author: fraidoon
'''
'''
Matrix multiplication
A matrix is a rectangle of numbers in rows and columns. 
A 1xN matrix has one row and N columns. An NxN matrix has N rows and N columns.

Multiplying a 1xN matrix A and an NxN matrix B produces a 
1xN matrix C. To determine the Nth element of C multiply the 
each element of A by each element of the Nth column of B and sum the results. 
Helpful information can be found at matrix multiplication.

Write a program that reads a 1xN matrix A and an NxN matrix B 
from input and outputs the 1xN matrix product, C. N can be of any size >= 2.

A is represented as a list of the integers found on the first line of input.
B is represented as a list of N rows, each of which is a list of N integers.
Each of the next N input lines contains the integers for one row of B.
Note: Input is one row at a time but multiplication uses columns of B.
For coding simplicity, follow each output integer by a space, even the last one. 
The output ends with a newline.

Ex: If the input is:

2 3
1 2
3 4
A contains 2 and 3, the first row of B contains 1 and 2, and the 
second row of B contains 3 and 4. The first element of C is (2 * 1) + (3 * 3), 
and the second element of C is (2 * 2) + (3 * 4). The program output is:

11 16

'''
# Input matrices
matrixA = []
matrixB = []
matrixC = []

# Read matrix A (1xN)
matrixA = list(map(int, input().split()))  # Read a single row as integers

# Determine the size of the matrix
N = len(matrixA)

# Read matrix B (NxN)
for i in range(N):
    row = list(map(int, input().split()))  # Read each row of B
    matrixB.append(row)

# Initialize matrix C (1xN) with zeros
matrixC = [0] * N

# Perform matrix multiplication
for j in range(N):  # For each column in matrix B
    for i in range(N):  # For each row in matrix B
        matrixC[j] += matrixA[i] * matrixB[i][j]

# Output matrix C
for val in matrixC:
    print(val, end=" ")
print()  # Newline at the end

