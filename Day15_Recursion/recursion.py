# Day 15 - Recursion


# 1. Countdown

def countdown(number):

    if number == 0:
        return

    print(number)

    countdown(number - 1)


print("Countdown:")
countdown(5)


# 2. Count Up

def count_up(number):

    if number == 0:
        return

    count_up(number - 1)

    print(number)


print("\nCount Up:")
count_up(5)


# 3. Factorial

def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print("\nFactorial:")
print(factorial(5))


# 4. Sum of Natural Numbers

def sum_numbers(n):

    if n == 0:
        return 0

    return n + sum_numbers(n - 1)


print("\nSum:")
print(sum_numbers(5))


# 5. Fibonacci

def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print("\nFibonacci:")

for i in range(8):
    print(fibonacci(i), end=" ")