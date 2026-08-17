'''1. Perfect Number

Problem:

Check whether N is perfect (sum of proper divisors equals number).

Input:

Integer N.

Output:

True or False.

Example:

Input: 6

Output:

True'''

n=int(input("enter:"))
sum=0

for i in range(1,n):
    if n% i==0:
        sum+=i
if sum==n:
    print(True)
else: print(False)