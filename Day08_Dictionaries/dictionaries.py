# Day 08 - Dictionaries

# Creating a Dictionary

student = {
    "name": "Aman",
    "age": 21,
    "branch": "CSE",
    "college": "ABC"
}

print("Student Dictionary:")
print(student)

print("\nAccessing Values")
print(student["name"])
print(student.get("age"))

print("\nAdding a New Key")
student["city"] = "Bhopal"
print(student)

print("\nUpdating a Value")
student["age"] = 22
print(student)

print("\nDictionary Methods")
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

print("\nRemoving an Item")
student.pop("city")
print(student)

print("\nLength")
print(len(student))

print("\nLoop Through Keys")
for key in student:
    print(key)

print("\nLoop Through Values")
for value in student.values():
    print(value)

print("\nLoop Through Key-Value Pairs")
for key, value in student.items():
    print(f"{key}: {value}")