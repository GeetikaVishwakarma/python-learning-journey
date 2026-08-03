# Day 06 - Tuples

# Creating Tuples

fruits = ("Apple", "Mango", "Orange", "Banana")
numbers = (10, 20, 30, 40, 50)
mixed = (100, "Python", 3.14, True)

print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed:", mixed)

print("\nAccessing Elements")
print(fruits[0])
print(fruits[-1])

print("\nTuple Slicing")
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])

print("\nLength")
print(len(fruits))

print("\nTuple Methods")

marks = (80, 90, 85, 90, 95)

print("Count of 90:", marks.count(90))
print("Index of 85:", marks.index(85))

print("\nLooping Through Tuple")

for fruit in fruits:
    print(fruit)

print("\nMembership Operators")
print("Apple" in fruits)
print("Grapes" not in fruits)

print("\nConcatenation")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print(tuple1 + tuple2)

print("\nRepetition")
print(tuple1 * 2)