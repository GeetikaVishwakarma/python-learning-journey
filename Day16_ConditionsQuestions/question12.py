##Take a number and check if it is a perfect square.
import math
n=int(input("enter a number :"))
root= math.sqrt(n)

if root==int(root):
    print("perfect square")
else: print("not a perfect square")    