'''7. Take a string and check:
    - If length < 5 → Short
    - 5–10 → Medium
    - 10 → Long'''

ch=input("enter : ")
if len(ch)<5:
    print("short")
elif 5<=len(ch)<10:
    print("medium")
else: print("long")