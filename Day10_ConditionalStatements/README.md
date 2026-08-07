# Day 10 – Conditional Statements (`if`, `elif`, `else`)

## 📖 Introduction

Conditional statements allow a program to make decisions based on specific conditions. They enable the program to execute different blocks of code depending on whether a condition is **True** or **False**.

Python provides three main conditional statements:

- `if`
- `if...else`
- `if...elif...else`

These statements are essential for building interactive and intelligent programs.

---

## 🎯 Learning Objectives

After completing this topic, I learned to:

- Understand conditional statements.
- Use the `if` statement.
- Use the `if...else` statement.
- Use the `if...elif...else` statement.
- Write nested conditional statements.
- Combine conditions using logical operators.

---

# 🧠 What is a Conditional Statement?

A conditional statement checks whether a condition is **True** or **False**.

If the condition is true, one block of code is executed; otherwise, another block is executed.

Example:

```python
age = 18

if age >= 18:
    print("Eligible to vote")
```

---

# 📌 The `if` Statement

Executes a block of code only when the condition is true.

```python
marks = 85

if marks >= 40:
    print("Pass")
```

---

# 📌 The `if...else` Statement

Executes one block if the condition is true and another block if it is false.

```python
age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

---

# 📌 The `if...elif...else` Statement

Used when multiple conditions need to be checked.

```python
marks = 78

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")
```

---

# 📌 Nested `if`

An `if` statement inside another `if` statement.

```python
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to Vote")
```

---

# 📌 Logical Operators

Logical operators can combine multiple conditions.

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry Allowed")
```

Logical Operators:

- `and`
- `or`
- `not`

---

# ✅ Key Takeaways

- Conditional statements help programs make decisions.
- `if` checks a single condition.
- `if...else` provides two possible outcomes.
- `if...elif...else` handles multiple conditions.
- Nested conditions allow more complex decision-making.
- Logical operators combine multiple conditions.