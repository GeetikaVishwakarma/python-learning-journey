# Day 12 - Break, Continue and Pass


# 1. Break Statement

print("Break Statement")

for i in range(1, 10):
    if i == 5:
        break

    print(i)


# 2. Continue Statement

print("\nContinue Statement")

for i in range(1, 6):
    if i == 3:
        continue

    print(i)


# 3. Pass Statement

print("\nPass Statement")

for i in range(1, 6):
    if i == 3:
        pass
    else:
        print(i)


# Break with While Loop

print("\nBreak with While Loop")

number = 1

while number <= 10:
    if number == 6:
        break

    print(number)
    number += 1


# Continue with While Loop

print("\nContinue with While Loop")

number = 0

while number < 5:
    number += 1

    if number == 3:
        continue

    print(number)


# Pass in Function

def future_function():
    pass


# Pass in Class

class Student:
    pass

print("\nProgram Completed")