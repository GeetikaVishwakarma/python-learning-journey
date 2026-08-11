# Day 13 – Functions

## 📖 Introduction

A **function** is a reusable block of code designed to perform a specific task.

Functions help make programs:

- Organized
- Reusable
- Easier to understand
- Easier to maintain
- Less repetitive

Instead of writing the same code multiple times, we can define a function once and call it whenever we need it.

---

## 🎯 Learning Objectives

After completing this topic, I learned to:

- Understand what a function is.
- Define and call functions.
- Use parameters and arguments.
- Use the `return` statement.
- Understand the difference between `print()` and `return`.
- Use default arguments.
- Use keyword arguments.
- Use `*args` and `**kwargs`.
- Understand local and global variables.

---

# 🧠 What is a Function?

A function is a reusable block of code that performs a particular task.

### Syntax

```python
def function_name():
    # code
```

Example:

```python
def greet():
    print("Hello, Python!")

greet()
```

Output:

```text
Hello, Python!
```

---

# 📌 Function Definition and Function Call

### Function Definition

Creating a function is called defining a function.

```python
def greet():
    print("Hello!")
```

### Function Call

Running the function is called calling the function.

```python
greet()
```

---

# 📥 Parameters and Arguments

A **parameter** is a variable defined inside the function definition.

An **argument** is the actual value passed to the function.

Example:

```python
def greet(name):
    print("Hello", name)

greet("Aman")
```

Here:

- `name` → Parameter
- `"Aman"` → Argument

---

# 🔙 Return Statement

The `return` statement sends a value back to the place where the function was called.

Example:

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

---

# 🖨️ `print()` vs `return`

### `print()`

Displays a value on the screen.

```python
def add(a, b):
    print(a + b)
```

### `return`

Sends a value back so it can be stored or used later.

```python
def add(a, b):
    return a + b

result = add(10, 20)
```

`return` is generally more useful when building reusable functions.

---

# 📌 Default Arguments

A default value can be assigned to a parameter.

```python
def greet(name="User"):
    print("Hello", name)

greet()
greet("Aman")
```

Output:

```text
Hello User
Hello Aman
```

---

# 🔑 Keyword Arguments

Arguments can be passed using parameter names.

```python
def student(name, age):
    print(name)
    print(age)

student(age=21, name="Aman")
```

The order does not matter when keyword arguments are used.

---

# 📦 `*args`

`*args` allows a function to accept multiple positional arguments.

```python
def add_numbers(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(add_numbers(10, 20, 30))
```

Output:

```text
60
```

---

# 📦 `**kwargs`

`**kwargs` allows a function to accept multiple keyword arguments.

```python
def student_info(**details):
    for key, value in details.items():
        print(key, ":", value)

student_info(
    name="Aman",
    age=21,
    branch="CSE"
)
```

---

# 🌍 Local and Global Variables

## Local Variable

A variable created inside a function is usually local to that function.

```python
def example():
    message = "Hello"
    print(message)
```

---

## Global Variable

A variable created outside a function has global scope.

```python
name = "Aman"

def greet():
    print(name)

greet()
```

---

# ✅ Key Takeaways

- Functions make code reusable.
- Functions are created using the `def` keyword.
- Parameters receive values passed as arguments.
- `return` sends a value back from a function.
- Default arguments provide fallback values.
- `*args` accepts multiple positional arguments.
- `**kwargs` accepts multiple keyword arguments.
- Functions help make programs cleaner and easier to maintain.