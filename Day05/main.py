# Day 5: Functions - Organizing Reusable Logic

# Define a simple function that says hello
def say_hello():
    print("Hello there!")
    print("Welcome to Day 5 :)")

# Call the function
say_hello()

# Function with parameters
def greet(name):
    print(f"Hi {name}, nice to meet you!")

greet("Min")
greet("Python Learner")

# Function that returns a value
def square(number):
    return number * number

result = square(5)
print("5 squared is", result)

# Multiple return values
def calculator(x, y):
    return x + y, x - y, x * y, x / y

add, sub, mul, div = calculator(10, 2)
print("Results:", add, sub, mul, div)
