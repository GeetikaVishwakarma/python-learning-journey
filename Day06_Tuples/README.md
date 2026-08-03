# Day 06 – Tuples

## 📖 Introduction

A **tuple** is an ordered collection of elements in Python. Similar to lists, tuples can store multiple values of different data types. However, unlike lists, tuples are **immutable**, which means their elements cannot be modified after creation.

Tuples are useful when you want to store data that should remain constant throughout the program.

---

## 🎯 Learning Objectives

After completing this topic, I learned to:

- Understand what a tuple is.
- Create tuples using different methods.
- Access tuple elements using indexing.
- Extract elements using slicing.
- Use built-in tuple methods.
- Perform common tuple operations.
- Understand the difference between lists and tuples.

---

# 🧠 What is a Tuple?

A tuple is an ordered and immutable collection of items enclosed in parentheses `()`.

Example:

```python
fruits = ("Apple", "Mango", "Orange")
```

---

# ✨ Features of Tuples

- Ordered collection
- Immutable (cannot be modified)
- Allows duplicate values
- Supports indexing and slicing
- Can store different data types

---

# 📝 Creating Tuples

```python
numbers = (10, 20, 30)

names = ("Alice", "Bob", "Charlie")

mixed = (100, "Python", 3.14, True)
```

A tuple with one element:

```python
single = (10,)
```

> **Note:** A comma is required to create a single-element tuple.

---

# 🔢 Tuple Indexing

Each element has an index.

```
Apple  Mango  Orange  Banana

0       1       2       3
```

Negative indexing:

```
Apple  Mango  Orange  Banana

-4      -3      -2      -1
```

Example:

```python
fruits = ("Apple", "Mango", "Orange")

print(fruits[0])
print(fruits[-1])
```

---

# ✂️ Tuple Slicing

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
```

---

# 🔧 Tuple Methods

Python provides only two built-in methods for tuples.

| Method | Description |
|---------|-------------|
| `count()` | Returns the number of occurrences of a value |
| `index()` | Returns the index of the first occurrence |

Example:

```python
numbers = (10, 20, 20, 30)

print(numbers.count(20))
print(numbers.index(30))
```

---

# 🔁 Iterating Through a Tuple

```python
fruits = ("Apple", "Mango", "Orange")

for fruit in fruits:
    print(fruit)
```

---

# 📊 List vs Tuple

| List | Tuple |
|------|-------|
| Mutable | Immutable |
| Uses `[]` | Uses `()` |
| More methods | Only `count()` and `index()` |
| Suitable for changing data | Suitable for fixed data |

---

# ✅ Key Takeaways

- Tuples are ordered collections.
- Tuples are immutable.
- They support indexing and slicing.
- Only `count()` and `index()` are available as built-in methods.
- Tuples are ideal for storing fixed or constant data.