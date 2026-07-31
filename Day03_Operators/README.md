# Day 03 – Operators

## 📖 Introduction

Operators are special symbols in Python that perform operations on variables and values. They are used to perform arithmetic calculations, compare values, assign values, and evaluate logical conditions.

Understanding operators is essential because they are used in almost every Python program.

---

## 🎯 Learning Objectives

After completing this topic, I learned to:

- Understand the purpose of operators.
- Use arithmetic operators for mathematical calculations.
- Compare values using comparison operators.
- Assign values using assignment operators.
- Perform logical operations using logical operators.
- Understand membership and identity operators.

---

# 🧠 What is an Operator?

An operator is a symbol that performs an operation on one or more operands.

Example:

```python
a = 10
b = 5

print(a + b)
```

Here,

- `+` is an operator.
- `a` and `b` are operands.

---

# 📚 Types of Operators in Python

## 1. Arithmetic Operators

Used to perform mathematical operations.

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `10 + 5 = 15` |
| `-` | Subtraction | `10 - 5 = 5` |
| `*` | Multiplication | `10 * 5 = 50` |
| `/` | Division | `10 / 5 = 2.0` |
| `//` | Floor Division | `10 // 3 = 3` |
| `%` | Modulus | `10 % 3 = 1` |
| `**` | Exponent | `2 ** 3 = 8` |

---

## 2. Comparison Operators

Used to compare two values.

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not Equal to |
| `>` | Greater Than |
| `<` | Less Than |
| `>=` | Greater Than or Equal To |
| `<=` | Less Than or Equal To |

Comparison operators always return either **True** or **False**.

---

## 3. Assignment Operators

Used to assign values to variables.

Examples:

```python
x = 10

x += 5
x -= 2
x *= 3
x /= 2
```

---

## 4. Logical Operators

Used to combine multiple conditions.

| Operator | Description |
|----------|-------------|
| `and` | Returns True if both conditions are True |
| `or` | Returns True if at least one condition is True |
| `not` | Reverses the result |

---

## 5. Membership Operators

Used to check whether a value exists in a sequence.

| Operator | Description |
|----------|-------------|
| `in` | Value exists |
| `not in` | Value does not exist |

Example:

```python
fruits = ["Apple", "Mango", "Orange"]

print("Apple" in fruits)
```

---

## 6. Identity Operators

Used to compare whether two variables refer to the same object.

| Operator | Description |
|----------|-------------|
| `is` | Same object |
| `is not` | Different object |

---

# ✅ Key Takeaways

- Operators perform operations on values.
- Arithmetic operators are used for calculations.
- Comparison operators return Boolean values.
- Assignment operators simplify value updates.
- Logical operators combine conditions.
- Membership and identity operators are useful when working with collections and objects.