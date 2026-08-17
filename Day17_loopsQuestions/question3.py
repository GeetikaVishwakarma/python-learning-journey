'''1. Multiplication Table

Problem:

Given an integer N, print its multiplication table up to 10.

Input:

Integer N.

Output:

N x 1 = …

…

N x 10 = …

Example:

Input: 3

Output:

3 x 1 = 3

3 x 2 = 6

...

3 x 10 = 30'''

n=int(input("enter:"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)