'''3. Take age and print:
    - "Child" if age < 13
    - "Teen" if age 13–19
    - "Adult" otherwise'''

age= int(input("enter a number : "))
if age<13:
    print("child")
elif 13<age<19:
    print("adult")
else: print("adult")