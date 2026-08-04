# Day 07 - Sets

# Creating Sets

fruits = {"Apple", "Mango", "Orange"}
numbers = {10, 20, 30, 40}
mixed = {100, "Python", 3.14, True}

print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed:", mixed)

print("\nAdding Elements")
fruits.add("Banana")
print(fruits)

print("\nRemoving Elements")
fruits.remove("Apple")
print(fruits)

fruits.discard("Mango")
print(fruits)

print("\nSet Operations")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)
print("Symmetric Difference:", A ^ B)

print("\nMembership")
print(2 in A)
print(10 not in A)

print("\nLength")
print(len(A))

print("\nLooping Through a Set")

for value in A:
    print(value)

print("\nRemoving Duplicates")

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = set(numbers)

print(unique_numbers)