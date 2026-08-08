# Day 11 - Loops

print("For Loop")

for i in range(1, 6):
    print(i)

print("\nLoop Through a String")

name = "Python"

for character in name:
    print(character)

print("\nLoop Through a List")

fruits = ["Apple", "Mango", "Banana"]

for fruit in fruits:
    print(fruit)

print("\nRange with Step")

for i in range(2, 11, 2):
    print(i)

print("\nWhile Loop")

count = 1

while count <= 5:
    print(count)
    count += 1

print("\nBreak Statement")

for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("\nContinue Statement")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("\nNested Loop")

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)