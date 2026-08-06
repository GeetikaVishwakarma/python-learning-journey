# Day 09 - Type Casting

print("Implicit Type Casting")

a = 10
b = 5.5

result = a + b

print(result)
print(type(result))

print("\nExplicit Type Casting")

number = "100"

print(type(number))

number = int(number)

print(number)
print(type(number))

print("\nInteger to Float")

num = 25

num = float(num)

print(num)
print(type(num))

print("\nFloat to Integer")

price = 99.99

price = int(price)

print(price)
print(type(price))

print("\nInteger to String")

age = 21

age = str(age)

print(age)
print(type(age))

print("\nString to List")

word = "Python"

letters = list(word)

print(letters)

print(type(letters))

print("\nList to Tuple")

numbers = [1, 2, 3]

print(tuple(numbers))

print("\nList to Set")

values = [1, 2, 2, 3, 3, 4]

print(set(values))

print("\nBoolean Conversion")

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))