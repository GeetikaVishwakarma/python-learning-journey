# Practice Questions – Functions

## Beginner

1. Create a function called `greet()` that prints `"Hello Python"`.

2. Create a function that takes a name as a parameter and prints:

```text
Hello Geetika
```

3. Create a function that takes two numbers and returns their sum.

4. Create a function that returns the square of a number.

---

## Intermediate

1. Create a function to find the largest of two numbers.

2. Create a function to check whether a number is even or odd.

3. Create a function to calculate the factorial of a number.

4. Create a function that accepts a student's name and marks and prints the details.

---

## Default Arguments

Create a function:

```python
def greet(name="User"):
```

Test it with:

- No argument
- Your name

---

## Keyword Arguments

Create a function that accepts:

- Name
- Age
- City

Call the function using keyword arguments.

---

## *args

Create a function that accepts any number of numbers and returns their sum.

Example:

```python
add_numbers(10, 20, 30, 40)
```

Expected output:

```text
100
```

---

## **kwargs

Create a function that accepts student details using `**kwargs`.

Example:

```python
student(
    name="Aman",
    age=21,
    branch="CSE"
)
```

---

## ⭐ Challenge

Create a simple calculator using functions.

Create separate functions for:

- Addition
- Subtraction
- Multiplication
- Division

Example:

```python
add(10, 5)
subtract(10, 5)
multiply(10, 5)
divide(10, 5)
```