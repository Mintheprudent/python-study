# Day 7: Looping with Lists (for 문 & 리스트 연습)

# Example 1: Creating a list
fruits = ["apple", "banana", "orange"]

# Example 2: Looping through the list
for fruit in fruits:
    print(f"I like {fruit}!")

# Example 3: Using range with for loop
for i in range(1, 4):
    print(f"This is loop number {i}")

# Example 4: List operations
numbers = [1, 2, 3]
numbers.append(4)     # [1, 2, 3, 4]
numbers.remove(2)     # [1, 3, 4]
print(numbers)
