'''1. Reverse a Number

Problem:

Reverse digits of integer N.

Input:

Integer N.

Output:

Reversed number.

Example:

Input: 123

Output:

321'''

n=int(input("enter:"))
rev=0
while n>0:
    digit=n%10
    rev=rev*10 +digit
    n=n//10
print(rev)

'''n=input("enter:")

print(n[::-1])'''