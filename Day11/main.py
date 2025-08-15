# Day 11 - File Handling
# Today we learned how to read from and write to files in Python.

# Writing to a file
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Hello, this is Day 11!\n")
    f.write("Learning Python file handling is fun.\n")

# Reading from a file
with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("=== File Content ===")
    print(content)

# Reading line by line
with open("example.txt", "r", encoding="utf-8") as f:
    print("=== Reading line by line ===")
    for line in f:
        print(line.strip())

# Appending to a file
with open("example.txt", "a", encoding="utf-8") as f:
    f.write("This line was added later.\n")

# Confirming append
with open("example.txt", "r", encoding="utf-8") as f:
    print("=== Updated File Content ===")
    print(f.read())
