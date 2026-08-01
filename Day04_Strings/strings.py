# Day 04 - Strings

text = "Python Programming"

print("Original String:", text)

print("\nIndexing")
print(text[0])
print(text[-1])

print("\nSlicing")
print(text[0:6])
print(text[7:])
print(text[:6])

print("\nLength")
print(len(text))

print("\nString Methods")
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

print("\nReplace")
print(text.replace("Python", "Java"))

print("\nSplit")
print(text.split())

print("\nFind")
print(text.find("Programming"))

print("\nCount")
print(text.count("m"))

print("\nConcatenation")
first = "Hello"
second = "Python"

print(first + " " + second)

print("\nRepetition")
print("Hi! " * 3)

print("\nMembership")
print("Python" in text)
print("Java" not in text)