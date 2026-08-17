'''1. Count Vowels

Problem:

Given a string S, count number of vowels.

Input:

String S.

Output:

Integer count.

Example:

Input: hello

Output:

2'''

s=input("enter :")
count=0
for i in s.lower():
   if i  in "aeiou":
      count+=1
print(count)