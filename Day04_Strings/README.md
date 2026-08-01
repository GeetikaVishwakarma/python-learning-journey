# Day 04 – Strings

## 📖 Introduction

A **string** is one of the most commonly used data types in Python. It is a sequence of characters enclosed in single quotes (`' '`), double quotes (`" "`), or triple quotes (`''' '''` or `""" """`).

Strings are immutable, which means their contents cannot be changed after they are created. However, Python provides many built-in methods to manipulate and work with strings efficiently.

---

## 🎯 Learning Objectives

After completing this topic, I learned to:

- Understand what a string is.
- Create strings using different quotation styles.
- Access characters using indexing.
- Extract parts of a string using slicing.
- Perform string operations.
- Use commonly used string methods.

---

# 🧠 What is a String?

A string is a collection (sequence) of characters.

Example:

```python
name = "Geetika"
```

The variable `name` stores a string value.

---

# 📝 Creating Strings

```python
name = "Python"
language = 'Programming'
message = """Welcome to Python"""
```

Python supports:

- Single Quotes (`' '`)
- Double Quotes (`" "`)
- Triple Quotes (`''' '''` or `""" """`)

---

# 🔢 String Indexing

Each character has an index.

```
P  y  t  h  o  n
0  1  2  3  4  5
```

Negative Indexing:

```
P  y  t  h  o  n
-6 -5 -4 -3 -2 -1
```

Example:

```python
word = "Python"

print(word[0])
print(word[-1])
```

---

# ✂️ String Slicing

Slicing extracts a part of a string.

Syntax:

```python
string[start:end]
```

Example:

```python
word = "Python"

print(word[0:3])
print(word[2:6])
print(word[:4])
print(word[3:])
```

---

# ➕ String Operations

Common operations:

- Concatenation (`+`)
- Repetition (`*`)
- Membership (`in`, `not in`)
- Length using `len()`

Example:

```python
first = "Hello"
second = "World"

print(first + " " + second)
```

---

# 🔧 Common String Methods

| Method | Description |
|---------|-------------|
| `upper()` | Converts to uppercase |
| `lower()` | Converts to lowercase |
| `title()` | Converts first letter of each word to uppercase |
| `capitalize()` | Capitalizes first letter |
| `strip()` | Removes extra spaces |
| `replace()` | Replaces text |
| `split()` | Splits a string into a list |
| `find()` | Finds the position of a substring |
| `count()` | Counts occurrences of a substring |

---

# ✅ Key Takeaways

- Strings store text data.
- Strings are immutable.
- Indexing accesses individual characters.
- Slicing extracts parts of a string.
- Python provides many useful string methods.