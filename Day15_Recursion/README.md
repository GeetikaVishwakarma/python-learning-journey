# Day 15 – Recursion

## 📖 Introduction

**Recursion** is a programming technique where a function calls itself to solve a problem.

A recursive function usually has two important parts:

1. **Base Case** – The condition that stops the recursion.
2. **Recursive Case** – The part where the function calls itself with a smaller or simpler input.

Recursion is useful for problems that can be divided into smaller versions of the same problem.

---

## 🎯 Learning Objectives

After completing this topic, I learned to:

- Understand recursion.
- Identify the base case.
- Understand the recursive case.
- Create recursive functions.
- Trace recursive function calls.
- Solve basic problems using recursion.
- Understand recursion depth.

---

# 🧠 What is Recursion?

Recursion occurs when a function calls itself.

Example:

```python
def countdown(number):

    if number == 0:
        return

    print(number)

    countdown(number - 1)


countdown(5)
```

Output:

```text
5
4
3
2
1
```

The function keeps calling itself until the base case is reached.

---

# 🛑 Base Case

The **base case** tells the function when to stop.

```python
if number == 0:
    return
```

Without a proper base case, the function may continue calling itself indefinitely.

---

# 🔄 Recursive Case

The recursive case is where the function calls itself.

```python
countdown(number - 1)
```

The input becomes smaller in each call, eventually reaching the base case.

---

# 📌 Recursion Example

## Factorial

The factorial of a number is:

```text
5! = 5 × 4 × 3 × 2 × 1
```

Recursive implementation:

```python
def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)
```

Example:

```python
print(factorial(5))
```

Output:

```text
120
```

---

# 📌 Sum of Natural Numbers

```python
def sum_numbers(n):

    if n == 0:
        return 0

    return n + sum_numbers(n - 1)


print(sum_numbers(5))
```

Output:

```text
15
```

Because:

```text
5 + 4 + 3 + 2 + 1 = 15
```

---

# 📌 Fibonacci Series

The Fibonacci sequence begins:

```text
0, 1, 1, 2, 3, 5, 8, 13...
```

Recursive implementation:

```python
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
```

Example:

```python
print(fibonacci(6))
```

Output:

```text
8
```

---

# 🔍 How Recursion Works

For:

```python
factorial(3)
```

The calls are:

```text
factorial(3)
    ↓
3 × factorial(2)
        ↓
        2 × factorial(1)
                ↓
                1
```

Then the results return:

```text
1
↓
2 × 1 = 2
↓
3 × 2 = 6
```

Therefore:

```text
3! = 6
```

---

# ⚠️ Recursion Limit

Python has a limit on how deeply a function can recursively call itself.

If recursion continues without reaching a base case, Python raises:

```text
RecursionError
```

Example of incorrect recursion:

```python
def infinite_recursion():
    infinite_recursion()
```

This function has no base case.

---

# 📊 Recursion vs Loop

| Recursion | Loop |
|-----------|------|
| Function calls itself | Repeats using loop |
| Needs a base case | Needs a loop condition |
| Can be easier for certain problems | Usually more memory efficient |
| Uses function call stack | Usually uses less stack memory |

---

# ✅ Key Takeaways

- Recursion means a function calls itself.
- Every recursive function needs a base case.
- The recursive case moves the problem toward the base case.
- Recursion uses the function call stack.
- Missing or incorrect base cases can cause `RecursionError`.
- Some problems are naturally suited to recursive solutions.