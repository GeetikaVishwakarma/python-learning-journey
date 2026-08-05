# Day 08 – Dictionaries

## 📖 Introduction

A **dictionary** is a built-in data structure in Python that stores data in **key-value pairs**. Each key in a dictionary is unique and is used to access its corresponding value.

Unlike lists and tuples, dictionaries do not use numeric indexes. Instead, values are accessed using their keys.

Dictionaries are widely used to represent structured data, such as student records, employee information, configuration settings, and JSON data.

---

## 🎯 Learning Objectives

After completing this topic, I learned to:

- Understand what a dictionary is.
- Create dictionaries using key-value pairs.
- Access values using keys.
- Add, update, and remove elements.
- Use common dictionary methods.
- Iterate through dictionaries.

---

# 🧠 What is a Dictionary?

A dictionary is a collection of **key-value pairs** enclosed in curly braces `{}`.

Example:

```python
student = {
    "name": "Aman",
    "age": 21,
    "branch": "CS"
}
```

Here,

- `"name"`, `"age"`, and `"branch"` are **keys**.
- `"Aman"`, `21`, and `"CS"` are **values**.

---

# ✨ Features of Dictionaries

- Stores data as key-value pairs.
- Keys are unique.
- Mutable (can be modified).
- Fast lookup using keys.
- Can store different data types.

---

# 📝 Creating Dictionaries

```python
student = {
    "name": "Aman",
    "age": 21,
    "college": "ABC"
}
```

Empty dictionary:

```python
student = {}
```

---

# 🔍 Accessing Values

```python
print(student["name"])
```

Or using `get()`:

```python
print(student.get("age"))
```

---

# ✏️ Adding and Updating Elements

Add a new key-value pair:

```python
student["city"] = "Bhopal"
```

Update an existing value:

```python
student["age"] = 22
```

---

# ❌ Removing Elements

```python
student.pop("city")
```

Other methods:

```python
student.popitem()
student.clear()
```

---

# 🔧 Common Dictionary Methods

| Method | Description |
|---------|-------------|
| `keys()` | Returns all keys |
| `values()` | Returns all values |
| `items()` | Returns key-value pairs |
| `get()` | Returns the value of a key |
| `update()` | Updates the dictionary |
| `pop()` | Removes a key |
| `popitem()` | Removes the last inserted item |
| `clear()` | Removes all items |

---

# 🔁 Iterating Through a Dictionary

Loop through keys:

```python
for key in student:
    print(key)
```

Loop through values:

```python
for value in student.values():
    print(value)
```

Loop through both:

```python
for key, value in student.items():
    print(key, value)
```

---

# ✅ Key Takeaways

- Dictionaries store data as key-value pairs.
- Keys must be unique.
- Dictionaries are mutable.
- Values are accessed using keys.
- Dictionary methods simplify data management.