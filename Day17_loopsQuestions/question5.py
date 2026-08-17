'''1. Reverse Counting

Problem:

Print numbers from N down to 1.

Input:

Integer N.

Output:

N to 1.

Example:

Input: 5

Output:

5 4 3 2 1'''

n=int(input("enter:"))
for i in range(n,0,-1):
    print(i,end=" ")