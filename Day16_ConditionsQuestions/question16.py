'''6. Take character input and check:
    - uppercase
    - lowercase
    - digit
    - special character'''

ch=input("enter :")
if ch.isupper():
    print("upercase")
elif ch.islower():
    print("lowercase")
elif ch.isdigit():
    print("digit")
else: print("special character")