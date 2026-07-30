# Day 02 – Data Types

## 📖 Introduction

In Python, every value has a data type. Data types define the kind of data a variable can store and determine the operations that can be performed on it.

Python is a dynamically typed language, which means the data type of a variable is automatically determined when a value is assigned.

---

## 🎯 Learning Objectives

After completing this topic, I learned to:

- Understand what data types are.
- Identify different built-in data types.
- Store different kinds of values in variables.
- Check the type of a variable using `type()`.
- Convert one data type into another using type casting.

---

## 🧠 What are Data Types?

A data type specifies the type of value stored in a variable.

Example:

```python
age = 21
```

Here, `21` is an integer (`int`).

---

# 📚 Built-in Data Types in Python

## 1. Integer (`int`)

Stores whole numbers.

```python
age = 21
```

Example values:

```
10
-5
1000
```

---

## 2. Float (`float`)

Stores decimal numbers.

```python
height = 5.6
```

Example values:

```
3.14
10.5
99.99
```

---

## 3. String (`str`)

Stores text enclosed in single or double quotes.

```python
name = "Geetika"
```

Example values:

```
"Python"
"Hello World"
```

---

## 4. Boolean (`bool`)

Stores either `True` or `False`.

```python
is_student = True
```

---

## 5. Complex (`complex`)

Stores complex numbers.

```python
number = 2 + 3j
```

---

# 🔍 Checking Data Types

Python provides the `type()` function.

Example:

```python
name = "Python"

print(type(name))
```

Output:

```
<class 'str'>
```

---

# 🔄 Type Casting

Type casting means converting one data type into another.

Example:

```python
age = "21"

age = int(age)
```

Common conversion functions:

- `int()`
- `float()`
- `str()`
- `bool()`

---

# ✅ Key Takeaways

- Every value has a data type.
- Python automatically detects data types.
- Use `type()` to check a variable's type.
- Type casting converts values from one type to another.
- Choosing the correct data type makes programs more efficient.