# Day 09 – Type Casting

## 📖 Introduction

**Type Casting** is the process of converting a value from one data type to another. Python provides built-in functions to perform these conversions easily.

Type casting is useful when working with user input, mathematical calculations, and data processing. It helps ensure that values are in the correct format before performing operations.

---

## 🎯 Learning Objectives

After completing this topic, I learned to:

- Understand what type casting is.
- Convert one data type into another.
- Perform implicit and explicit type casting.
- Use Python's built-in conversion functions.
- Handle data conversion safely.

---

# 🧠 What is Type Casting?

Type casting means converting a value from one data type to another.

Example:

```python
age = "21"

age = int(age)
```

Now, `age` becomes an integer instead of a string.

---

# 📚 Types of Type Casting

## 1. Implicit Type Casting

Python automatically converts one data type into another when needed.

Example:

```python
num1 = 10
num2 = 5.5

result = num1 + num2

print(result)
print(type(result))
```

Output:

```
15.5
<class 'float'>
```

---

## 2. Explicit Type Casting

The programmer manually converts one data type into another using built-in functions.

Example:

```python
age = "21"

age = int(age)

print(age)
```

---

# 🔧 Built-in Type Casting Functions

| Function | Description | Example |
|----------|-------------|---------|
| `int()` | Converts to Integer | `int("10")` |
| `float()` | Converts to Float | `float(5)` |
| `str()` | Converts to String | `str(100)` |
| `bool()` | Converts to Boolean | `bool(1)` |
| `list()` | Converts to List | `list("Python")` |
| `tuple()` | Converts to Tuple | `tuple([1,2,3])` |
| `set()` | Converts to Set | `set([1,2,2,3])` |

---

# 🔄 Common Type Conversions

## String to Integer

```python
number = "100"

print(int(number))
```

---

## Integer to Float

```python
num = 50

print(float(num))
```

---

## Float to Integer

```python
price = 45.9

print(int(price))
```

> **Note:** The decimal part is removed, not rounded.

---

## Integer to String

```python
age = 21

print(str(age))
```

---

## String to List

```python
word = "Python"

print(list(word))
```

Output:

```
['P', 'y', 't', 'h', 'o', 'n']
```

---

# ⚠️ Invalid Type Casting

Not all conversions are valid.

Example:

```python
number = "Python"

int(number)
```

This raises:

```
ValueError
```

because `"Python"` cannot be converted into an integer.

---

# ✅ Key Takeaways

- Type casting converts one data type into another.
- Python supports implicit and explicit type casting.
- Built-in functions simplify data conversion.
- Invalid conversions raise errors.
- Choosing the correct data type helps write reliable programs.