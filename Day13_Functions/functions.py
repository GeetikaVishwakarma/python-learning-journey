# Day 13 - Functions


# 1. Simple Function

def greet():
    print("Hello, Python!")


greet()


# 2. Function with Parameter

def greet_user(name):
    print("Hello", name)


greet_user("Aman")


# 3. Function with Multiple Parameters

def add(a, b):
    return a + b


result = add(10, 20)
print("Addition:", result)


# 4. Return Statement

def square(number):
    return number * number


print("Square:", square(5))


# 5. Default Argument

def welcome(name="User"):
    print("Welcome", name)


welcome()
welcome("Aman")


# 6. Keyword Arguments

def student(name, age, branch):
    print("Name:", name)
    print("Age:", age)
    print("Branch:", branch)


student(
    branch="CSE",
    age=21,
    name="Aman"
)


# 7. *args

def add_numbers(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


print("Total:", add_numbers(10, 20, 30, 40))


# 8. **kwargs

def student_info(**details):
    for key, value in details.items():
        print(key, ":", value)


student_info(
    name="Aman",
    age=21,
    branch="CSE"
)


# 9. Local Variable

def local_example():
    message = "This is a local variable"
    print(message)


local_example()


# 10. Global Variable

name = "Aman"


def global_example():
    print("Name:", name)


global_example()