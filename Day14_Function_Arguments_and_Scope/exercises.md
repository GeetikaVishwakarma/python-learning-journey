# Practice Questions – Function Arguments and Scope

## Positional Arguments

1. Create a function that accepts a student's name and age.
2. Call the function using positional arguments.

---

## Keyword Arguments

Create a function that accepts:

- Name
- Age
- City

Call the function using keyword arguments.

Example:

```python
student(
    city="Bhopal",
    name="Geetika",
    age=21
)
```

---

## Default Arguments

Create a function:

```python
def greet(name="User"):
```

Call it:

1. Without an argument.
2. With your name.

---

## `*args`

Create a function that accepts any number of numbers and returns:

- Sum
- Maximum number
- Minimum number

Example:

```python
calculate(10, 20, 30, 40)
```

---

## `**kwargs`

Create a function that accepts student information using `**kwargs`.

Example:

```python
student(
    name="Geetika",
    age=21,
    branch="ECE",
    college="LNCT"
)
```

Print each key and value.

---

## Local and Global Scope

1. Create a global variable called `college`.
2. Create a function that prints the global variable.
3. Create a local variable inside another function.
4. Try accessing the local variable outside the function and observe what happens.

---

## ⭐ Challenge

Create a function called `calculate_marks()` that accepts any number of marks using `*args`.

The function should return:

- Total marks
- Average marks
- Highest mark
- Lowest mark

Example:

```python
calculate_marks(80, 75, 90, 85, 95)
```