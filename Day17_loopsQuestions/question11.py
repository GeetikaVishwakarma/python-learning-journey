'''1. Fibonacci Series

Problem:

Print first N Fibonacci numbers.

Input:

Integer N.

Output:

Sequence.

Example:

Input: 5

Output:

0 1 1 2 3'''

n=int(input("enter : "))
a=0
b=1
for i in range(n):
    print(a, end=" ")
    c=a+b
    a=b
    b=c