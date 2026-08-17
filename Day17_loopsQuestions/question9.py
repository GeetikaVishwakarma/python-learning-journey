'''1. Factorial

Problem:

Compute factorial of N using loop.

Input:

Integer N.

Output:

Factorial value.

Example:

Input: 5

Output:

120'''

n=int(input("enter:"))
fact=1

for i in range(1, n+1):
    fact=fact*i

print(fact)