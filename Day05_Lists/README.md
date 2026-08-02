# Day 05 – Lists

## 📖 Introduction

A **list** is one of the most versatile and widely used data structures in Python. It is an ordered, mutable collection that allows storing multiple items in a single variable. Lists can contain elements of the same or different data types and support a wide range of built-in operations and methods.

Lists are commonly used to manage collections of data such as names, numbers, marks, products, or any sequence of values.

---

## 🎯 Learning Objectives

After completing this topic, I learned to:

- Understand what a list is.
- Create and initialize lists.
- Access list elements using indexing.
- Extract elements using slicing.
- Modify list elements.
- Use common list methods.
- Iterate through lists using loops.

---

# 🧠 What is a List?

A list is an ordered collection of items enclosed in square brackets `[]`.

Example:

```python
fruits = ["Apple", "Mango", "Orange"]
```

Lists can store multiple values in a single variable.

---

# ✨ Features of Lists

- Ordered collection
- Mutable (can be modified)
- Allows duplicate values
- Can store different data types
- Supports indexing and slicing

---

# 📝 Creating Lists

```python
numbers = [10, 20, 30, 40]

names = ["Alice", "Bob", "Charlie"]

mixed = [10, "Python", 3.14, True]
```

---

# 🔢 List Indexing

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
fruits = ["Apple", "Mango", "Orange"]

print(fruits[0])
print(fruits[-1])
```

---

# ✂️ List Slicing

Slicing extracts a portion of a list.

```python
numbers = [10,20,30,40,50]

print(numbers[1:4])

print(numbers[:3])

print(numbers[2:])
```

---

# ✏️ Modifying Lists

Lists are mutable.

```python
fruits = ["Apple", "Mango", "Orange"]

fruits[1] = "Banana"

print(fruits)
```

---

# 🔧 Common List Methods

| Method | Description |
|---------|-------------|
| `append()` | Adds an element at the end |
| `insert()` | Inserts an element at a specified index |
| `remove()` | Removes the first matching element |
| `pop()` | Removes an element by index |
| `clear()` | Removes all elements |
| `sort()` | Sorts the list |
| `reverse()` | Reverses the list |
| `count()` | Counts occurrences of an element |
| `index()` | Returns the index of an element |
| `copy()` | Creates a shallow copy of the list |

---

# 🔁 Iterating Through a List

```python
fruits = ["Apple", "Mango", "Orange"]

for fruit in fruits:
    print(fruit)
```

---

# ✅ Key Takeaways

- Lists store multiple values in one variable.
- Lists maintain the order of elements.
- Lists are mutable.
- Lists support indexing and slicing.
- Built-in methods make list operations simple and efficient.