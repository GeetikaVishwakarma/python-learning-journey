# Day 05 - Lists

# Creating Lists

fruits = ["Apple", "Mango", "Orange", "Banana"]
numbers = [10, 20, 30, 40, 50]
mixed = [100, "Python", 3.14, True]

print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed:", mixed)

print("\nAccessing Elements")
print(fruits[0])
print(fruits[-1])

print("\nList Slicing")
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])

print("\nUpdating Elements")
fruits[1] = "Pineapple"
print(fruits)

print("\nAppending")
fruits.append("Grapes")
print(fruits)

print("\nInserting")
fruits.insert(2, "Kiwi")
print(fruits)

print("\nRemoving")
fruits.remove("Apple")
print(fruits)

print("\nPopping")
fruits.pop()
print(fruits)

print("\nSorting")
numbers.sort()
print(numbers)

print("\nReversing")
numbers.reverse()
print(numbers)

print("\nLength")
print(len(fruits))

print("\nLooping Through a List")

for fruit in fruits:
    print(fruit)