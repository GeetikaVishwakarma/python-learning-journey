# Day 14 – Function Arguments and Scope

## 📖 Introduction

Functions become more powerful when we can pass different values to them and control where variables can be accessed.

In this topic, I learned about different types of function arguments and variable scope in Python.

---

## 🎯 Learning Objectives

After completing this topic, I learned to:

- Understand positional arguments.
- Use keyword arguments.
- Use default arguments.
- Understand variable-length arguments.
- Use `*args`.
- Use `**kwargs`.
- Understand local and global scope.
- Understand the `global` keyword.
- Understand how function arguments work.

---

# 📌 1. Positional Arguments

Arguments are matched with parameters based on their position.

```python
def student(name, age):
    print(name)
    print(age)

student("Geetika", 21)
```

Here:

- `"Geetika"` is passed to `name`.
- `21` is passed to `age`.

---

# 🔑 2. Keyword Arguments

Arguments can be passed using parameter names.

```python
def student(name, age):
    print(name)
    print(age)

student(age=21, name="Geetika")
```

The order does not matter when using keyword arguments.

---

# ⚙️ 3. Default Arguments

A parameter can have a default value.

```python
def greet(name="User"):
    print("Hello", name)

greet()
greet("Geetika")
```

Output:

```text
Hello User
Hello Geetika
```

---

# 📦 4. `*args`

`*args` allows a function to accept any number of positional arguments.

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

Inside the function, `numbers` behaves like a tuple.

---

# 📦 5. `**kwargs`

`**kwargs` allows a function to accept any number of keyword arguments.

```python
def student_info(**details):
    for key, value in details.items():
        print(key, ":", value)

student_info(
    name="Geetika",
    age=21,
    branch="ECE"
)
```

Inside the function, `details` behaves like a dictionary.

---

# 🌍 6. Local Scope

A variable created inside a function is generally available only inside that function.

```python
def example():
    message = "Hello"
    print(message)

example()
```

The variable `message` is local to the function.

---

# 🌎 7. Global Scope

A variable created outside a function has global scope.

```python
name = "Geetika"

def greet():
    print(name)

greet()
```

The function can access the global variable.

---

# 🔄 8. Global Keyword

The `global` keyword allows a function to modify a global variable.

```python
count = 10

def update_count():
    global count
    count = 20

update_count()

print(count)
```

Output:

```text
20
```

---

# 📊 Types of Arguments

| Type | Example |
|------|---------|
| Positional | `student("Geetika", 21)` |
| Keyword | `student(name="Geetika", age=21)` |
| Default | `greet(name="User")` |
| Variable Positional | `add(*numbers)` |
| Variable Keyword | `student(**details)` |

---

# ✅ Key Takeaways

- Positional arguments depend on order.
- Keyword arguments use parameter names.
- Default arguments provide default values.
- `*args` accepts multiple positional arguments.
- `**kwargs` accepts multiple keyword arguments.
- Local variables belong to their function.
- Global variables can be accessed from different parts of a program.
- The `global` keyword allows modification of a global variable.