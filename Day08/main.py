# Day 8 - Functions
# Today we learned how to define and use functions in Python.

# Simple function
def greet():
    print("Hello, welcome to Day 8!")

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}! Welcome to Day 8.")

# Function with return value
def add_numbers(a, b):
    return a + b

# Calling the functions
greet()
greet_person("Alice")
result = add_numbers(5, 3)
print(f"The sum is {result}")
