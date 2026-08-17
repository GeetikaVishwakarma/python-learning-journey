'''1. Square Series

Problem:

Print squares of numbers from 1 to N.

Input:

Integer N.

Output:

Sequence of squares.

Example:

Input: 4

Output:

1 4 9 16'''

n=int(input("enter:"))

for i in range(1,n+1):
    print(i*i, end=" ")