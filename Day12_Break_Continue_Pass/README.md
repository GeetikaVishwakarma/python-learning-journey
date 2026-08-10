# Day 12 – Break, Continue and Pass

## 📖 Introduction

Python provides special control statements that change the normal flow of loops and code execution.

The three important statements are:

- `break`
- `continue`
- `pass`

These statements are especially useful when working with loops and conditional statements.

---

## 🎯 Learning Objectives

After completing this topic, I learned to:

- Understand the `break` statement.
- Use `break` to terminate a loop.
- Understand the `continue` statement.
- Use `continue` to skip an iteration.
- Understand the `pass` statement.
- Use `pass` as a placeholder in Python programs.

---

# 🛑 1. Break Statement

The `break` statement immediately terminates the loop.

### Example

```python
for i in range(1, 10):
    if i == 5:
        break

    print(i)
```

Output:

```text
1
2
3
4
```

When `i` becomes `5`, the `break` statement stops the loop.

---

# ⏭️ 2. Continue Statement

The `continue` statement skips the current iteration and moves to the next iteration of the loop.

### Example

```python
for i in range(1, 6):
    if i == 3:
        continue

    print(i)
```

Output:

```text
1
2
4
5
```

The number `3` is skipped.

---

# ⏸️ 3. Pass Statement

The `pass` statement does nothing.

It is used as a placeholder when a statement is required syntactically but you don't want to execute any code yet.

### Example

```python
for i in range(5):
    if i == 2:
        pass
    else:
        print(i)
```

`pass` allows the program to continue without performing any action.

---

# 🔄 Break vs Continue vs Pass

| Statement | Purpose |
|-----------|---------|
| `break` | Terminates the loop |
| `continue` | Skips the current iteration |
| `pass` | Does nothing; acts as a placeholder |

---

# 📌 Break with While Loop

```python
number = 1

while number <= 10:
    if number == 6:
        break

    print(number)
    number += 1
```

---

# 📌 Continue with While Loop

```python
number = 0

while number < 5:
    number += 1

    if number == 3:
        continue

    print(number)
```

---

# 📌 Pass in a Function

`pass` can also be used when creating a function that you want to implement later.

```python
def calculate_result():
    pass
```

---

# 📌 Pass in a Class

```python
class Student:
    pass
```

This creates a class without adding any implementation yet.

---

# ✅ Key Takeaways

- `break` completely stops a loop.
- `continue` skips the current iteration.
- `pass` performs no action.
- `break` and `continue` are mainly used to control loops.
- `pass` is useful as a placeholder for future code.