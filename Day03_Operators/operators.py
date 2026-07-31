# Day 03 - Operators

a = 10
b = 3

print("Arithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

print("\nComparison Operators")
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal:", a >= b)
print("Less Than or Equal:", a <= b)

print("\nAssignment Operators")
x = 10
x += 5
print("x += 5:", x)

x -= 3
print("x -= 3:", x)

print("\nLogical Operators")
print(True and False)
print(True or False)
print(not True)

print("\nMembership Operators")
fruits = ["Apple", "Mango", "Orange"]

print("Apple" in fruits)
print("Banana" not in fruits)

print("\nIdentity Operators")

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print(list1 is list2)
print(list1 is list3)
print(list1 is not list3)