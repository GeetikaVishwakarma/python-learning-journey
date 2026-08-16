##Take a number and check if it is 1-digit, 2-digit, or 3-digit.
n=int(input("enter a number: "))
n=abs(n)
if n <=9:
    print("1 digit")
elif 10<=n<=99:
    print("2 digit")
elif 100<=n<=999:
    print("3-digit")
else: print("grater than 3-digit")

