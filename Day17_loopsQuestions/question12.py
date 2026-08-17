'''1. Prime Check

Problem:

Determine if N is prime.

Input:

Integer N.

Output:

True or False.

Example:

Input: 7

Output:

True'''

n=int(input("enter :"))

if n<2:
    print(False)
else:
    is_prime=True
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            is_prime=False
            break
    print(is_prime)
