#Take a number and check if it is divisible by 3, 5, or both.

n=int(input("enter a number:"))

if n%3==0 and n%5==0:
    print("divisible by both")
elif n%3==0:
    print("divisible only by 3")
elif n%5==0:
    print("divisible by 5") 
else: print("invalid")    