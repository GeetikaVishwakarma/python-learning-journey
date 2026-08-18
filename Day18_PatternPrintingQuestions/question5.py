'''
0
0 1
0 1 2
0 1 2 3
'''

n=int(input("enter:"))

for i in range(1, n+1):
    for j in range(i):
        print(j, end=" ")
    print()