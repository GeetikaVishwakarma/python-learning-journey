'''1. Count Uppercase and Lowercase

Problem:

Given string S, count uppercase and lowercase characters.

Input:

String S.

Output:

Two integers.

Example:

Input: PyThOn

Output:

Uppercase: 3

Lowercase: 3'''

s = input("Enter: ")

l = 0
u = 0

for i in s:
    if i.isupper():
        u += 1
    elif i.islower():
        l += 1

print("Uppercase", u)
print("Lowercase", l)