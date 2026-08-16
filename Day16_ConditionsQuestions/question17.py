#Take a number and check Armstrong number (3-digit).

n=int(input("enter : "))

original=n
sum=0

while n>0:
    digit = n%10
    sum= sum +digit **3
    n= n//10
if sum== original:
    print("armstrong number ")
else: print("not an armstrong number")