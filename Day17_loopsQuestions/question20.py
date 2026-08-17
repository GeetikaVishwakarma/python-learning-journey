'''1. Strong Number

Problem:

Check if N is Strong number (sum of factorial of digits equals number).

Input:

Integer N.

Output:

True or False.

Example:

Input: 145

Output:

True

What is a Strong Number?

A Strong Number is a number where the sum of the factorials of its digits is equal to the original number.
'''

n=int(input("enter:"))

original=n
total=0

while n>0:
    digit =n%10

    fact=1
    for i in range(1,digit+1):
        fact *=i

    total +=fact
    n//=10

if total == original:
    print(True)
else: print(False)


