# Day 07 – Sets

## 📖 Introduction

A **set** is an unordered collection of unique elements in Python. Unlike lists and tuples, sets do not allow duplicate values and do not maintain the order of elements.

Sets are highly efficient for checking membership, removing duplicates, and performing mathematical set operations such as union, intersection, and difference.

---

## 🎯 Learning Objectives

After completing this topic, I learned to:

- Understand what a set is.
- Create sets using different methods.
- Add and remove elements.
- Perform common set operations.
- Use built-in set methods.
- Understand the difference between sets, lists, and tuples.

---

# 🧠 What is a Set?

A set is a collection of **unique** elements enclosed in curly braces `{}`.

Example:

```python
fruits = {"Apple", "Mango", "Orange"}
```

---

# ✨ Features of Sets

- Unordered collection
- Mutable (elements can be added or removed)
- Does not allow duplicate values
- Supports mathematical set operations
- Efficient for membership testing

---

# 📝 Creating Sets

```python
numbers = {10, 20, 30}

fruits = {"Apple", "Mango", "Orange"}

mixed = {10, "Python", 3.14, True}
```

Creating an empty set:

```python
empty_set = set()
```

> **Note:** `{}` creates an empty dictionary, not an empty set.

---

# ➕ Adding Elements

```python
fruits.add("Banana")
```

---

# ➖ Removing Elements

```python
fruits.remove("Apple")
```

Other useful methods:

```python
fruits.discard("Mango")
fruits.pop()
fruits.clear()
```

---

# 🔧 Common Set Methods

| Method | Description |
|---------|-------------|
| `add()` | Adds an element |
| `remove()` | Removes an element (raises an error if not found) |
| `discard()` | Removes an element safely |
| `pop()` | Removes a random element |
| `clear()` | Removes all elements |
| `copy()` | Creates a copy of the set |

---

# 🔄 Set Operations

## Union

```python
A = {1,2,3}
B = {3,4,5}

print(A | B)
```

---

## Intersection

```python
print(A & B)
```

---

## Difference

```python
print(A - B)
```

---

## Symmetric Difference

```python
print(A ^ B)
```

---

# 🔁 Iterating Through a Set

```python
fruits = {"Apple", "Mango", "Orange"}

for fruit in fruits:
    print(fruit)
```

---

# 📊 List vs Tuple vs Set

| Feature | List | Tuple | Set |
|----------|------|-------|-----|
| Ordered | ✅ | ✅ | ❌ |
| Mutable | ✅ | ❌ | ✅ |
| Allows Duplicates | ✅ | ✅ | ❌ |
| Indexing | ✅ | ✅ | ❌ |

---

# ✅ Key Takeaways

- Sets store only unique elements.
- Sets are unordered.
- Sets are mutable.
- Sets are ideal for removing duplicates.
- Union, intersection, difference, and symmetric difference are powerful set operations.