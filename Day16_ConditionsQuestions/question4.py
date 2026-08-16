"""4. Take marks and print:
    - "Fail" if < 35
    - "Pass" if 35–59
    - "First Class" if 60–79
    - "Distinction" if 80+"""

marks=int(input("enetr a numberc :"))
if marks<35:
    print("fail")
elif 35<=marks<=59:
    print("pass")
elif 60<=marks<=79:
    print("first class")
else:print("distinction")