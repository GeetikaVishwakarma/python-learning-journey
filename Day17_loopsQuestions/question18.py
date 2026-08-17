'''1. Palindrome Number

Problem:

Check whether N is palindrome.

Input:

Integer N.

Output:

True or False.

Example:

Input: 121

Output:

True'''

n=input("enter :")

if n==n[::-1]:
    print(True)
else: 
    print(False)
