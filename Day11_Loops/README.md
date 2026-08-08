# Day 11 – Loops

## 📖 Introduction

Loops are used to execute a block of code repeatedly. They help reduce code repetition and are especially useful when working with collections of data or when a task needs to be performed multiple times.

Python provides two main types of loops:

- `for` loop
- `while` loop

---

## 🎯 Learning Objectives

After completing this topic, I learned to:

- Understand the purpose of loops.
- Use `for` loops to iterate over sequences.
- Use `while` loops when a condition controls repetition.
- Use `range()` with `for` loops.
- Use `break` and `continue`.
- Understand nested loops.

---

# 🧠 What is a Loop?

A loop repeatedly executes a block of code until a specified condition is met.

Example:

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

---

# 🔵 For Loop

A `for` loop is used to iterate over a sequence such as a string, list, tuple, set, or dictionary.

Example:

```python
fruits = ["Apple", "Mango", "Banana"]

for fruit in fruits:
    print(fruit)
```

---

# 🔢 Using `range()`

The `range()` function generates a sequence of numbers.

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

### `range(start, stop, step)`

```python
for i in range(1, 10, 2):
    print(i)
```

Output:

```text
1
3
5
7
9
```

---

# 🟢 While Loop

A `while` loop repeatedly executes a block of code as long as a condition is `True`.

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

# 🛑 Break Statement

The `break` statement stops the loop immediately.

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

---

# ⏭️ Continue Statement

The `continue` statement skips the current iteration and moves to the next iteration.

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

---

# 🔁 Nested Loops

A loop inside another loop is called a nested loop.

Example:

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

Nested loops are commonly used for patterns and working with two-dimensional data.

---

# ✅ Key Takeaways

- Loops help repeat code efficiently.
- `for` loops are useful for iterating over sequences.
- `while` loops execute while a condition remains true.
- `range()` is commonly used with `for` loops.
- `break` stops a loop.
- `continue` skips an iteration.
- Nested loops contain one loop inside another.