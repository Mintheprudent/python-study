# Day 8 - Functions

Today, I learned how to **create and use functions** in Python.  
Functions let you group code into reusable blocks, which helps keep programs clean and easy to read.

## Key Takeaways
- Use `def` to define a function.
- Functions can have **parameters** to pass in data.
- Functions can **return** a value using the `return` keyword.
- Calling a function executes the code inside it.

### Example
```python
def greet():
    print("Hello, welcome to Day 8!")

def greet_person(name):
    print(f"Hello, {name}! Welcome to Day 8.")

def add_numbers(a, b):
    return a + b

greet()
greet_person("Alice")
result = add_numbers(5, 3)
print(f"The sum is {result}")
