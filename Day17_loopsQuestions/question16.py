'''1. Sum of Even and Odd Separately

Problem:

Given N, compute sum of even and odd numbers from 1 to N separately.

Input:

Integer N.

Output:

Two integers.

Example:

Input: 5

Output:

Even: 6

Odd: 9'''

n=int(input("enter: "))
even=0
odd=0
for i in range(1, n+1):
    if i %2==0:
        even +=i
    else:
        odd +=i
print("even:", even)
print("odd:", odd)