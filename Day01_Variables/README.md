# Day 01 – Variables

## 📖 Introduction

Variables are the fundamental building blocks of Python programming. They are used to store data that can be accessed, modified, and reused throughout a program.

Unlike many programming languages, Python does not require you to declare the data type of a variable explicitly. The type is automatically determined based on the assigned value.

---

## 🎯 Learning Objectives

After completing this topic, I learned to:

- Understand what a variable is.
- Create and assign values to variables.
- Follow Python variable naming rules.
- Use meaningful variable names.
- Reassign values to variables.
- Check the data type of a variable using `type()`.

---

## 🧠 What is a Variable?

A variable is a named memory location used to store data.

Think of a variable as a labeled container that holds information.

Example:

```python
name = "Geetika"
```

Here,

- `name` → Variable Name
- `=` → Assignment Operator
- `"Geetika"` → Value

---

## 📝 Variable Naming Rules

- Variable names can contain letters, numbers, and underscores (`_`).
- Variable names cannot start with a number.
- Variable names are case-sensitive.
- Spaces are not allowed.
- Python keywords cannot be used as variable names.

### ✅ Valid Variable Names

```python
name
student_name
age2
total_marks
```

### ❌ Invalid Variable Names

```python
2name
student name
class
my-name
```

---

## 💡 Best Practices

- Use meaningful names.
- Follow the `snake_case` naming convention.
- Keep names simple and descriptive.

Example:

```python
student_name = "Geetika"
total_marks = 480
```

instead of

```python
a = "Geetika"
b = 480
```

---

## 🔄 Variable Reassignment

Variables can store new values at any time.

```python
age = 20
age = 21

print(age)
```

Output:

```
21
```

---

## 🔍 Checking Variable Type

Python provides the `type()` function to check the type of a variable.

```python
name = "Geetika"

print(type(name))
```

Output:

```
<class 'str'>
```

---

## 📂 Files Included

| File | Description |
|------|-------------|
| `variables.py` | Examples demonstrating variables |
| `exercises.md` | Practice questions for variables |

---

## ✅ Key Takeaways

- Variables store data.
- Python is dynamically typed.
- Variable names should be meaningful.
- Variables can be reassigned.
- Use `type()` to identify a variable's data type.