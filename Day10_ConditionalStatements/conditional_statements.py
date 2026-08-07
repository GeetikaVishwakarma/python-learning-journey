# Day 10 - Conditional Statements

print("Simple if")

age = 20

if age >= 18:
    print("Eligible to Vote")

print("\nif...else")

number = 7

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

print("\nif...elif...else")

marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")

print("\nNested if")

age = 22
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")
    else:
        print("License required.")
else:
    print("Not eligible to drive.")

print("\nLogical Operators")

username = "admin"
password = "python123"

if username == "admin" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Credentials")