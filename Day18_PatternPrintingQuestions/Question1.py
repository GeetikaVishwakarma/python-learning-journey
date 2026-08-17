'''1. Pattern Printing – Increasing Stars

Problem:

Print pattern:

Input: 4

Output:

*

** '''

n = int(input("Enter: "))

for i in range(1, n + 1):
    print("*" * i)