'''1. Print All Factors

Problem:

Print all factors of N.

Input:

Integer N.

Output:

Factors in ascending order.

Example:

Input: 6

Output:

1 2 3 6'''

n=int(input("enter:"))

for i in range(1,n+1):
    if n%i==0:
        print(i, end=" ")