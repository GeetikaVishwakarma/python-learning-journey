# Day 14 - Function Arguments and Scope


# 1. Positional Arguments

def student(name, age):
    print("Name:", name)
    print("Age:", age)


student("Geetika", 21)


# 2. Keyword Arguments

print("\nKeyword Arguments")

student(age=21, name="Geetika")


# 3. Default Arguments

print("\nDefault Arguments")


def greet(name="User"):
    print("Hello", name)


greet()
greet("Geetika")


# 4. *args

print("\n*args")


def add_numbers(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


print(add_numbers(10, 20))
print(add_numbers(10, 20, 30, 40))


# 5. **kwargs

print("\n**kwargs")


def student_info(**details):
    for key, value in details.items():
        print(key, ":", value)


student_info(
    name="Geetika",
    age=21,
    branch="ECE"
)


# 6. Local Scope

print("\nLocal Scope")


def local_example():
    message = "This is a local variable"
    print(message)


local_example()


# 7. Global Scope

print("\nGlobal Scope")

name = "Geetika"


def global_example():
    print("Name:", name)


global_example()


# 8. Global Keyword

print("\nGlobal Keyword")

count = 10


def update_count():
    global count
    count = 20


print("Before:", count)

update_count()

print("After:", count)