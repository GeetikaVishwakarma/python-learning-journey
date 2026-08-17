'''1. Largest Digit

Problem:

Find largest digit in N.

Input:

Integer N.

Output:

Largest digit.

Example:

Input: 5482

Output:

8'''

'''n=input("enter :")
l=0
for i in n:
    if int(i)>l:
        l=int(i)
print(l)'''

n=input("enter :")
l=0
for i in n:
    digit=int(i)
    if digit>l:
        l=digit
print(l)