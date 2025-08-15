## Day 11 - File Handling

Today, I learned how to **create, read, write, and append** files in Python.  
File handling is essential for saving and loading data in real programs.

## Key Takeaways
- Use `open(filename, mode, encoding)` to work with files.
- Common modes:  
  - `"r"` → read  
  - `"w"` → write (overwrites file)  
  - `"a"` → append (adds to file)  
- Always close files after use — or better, use `with open(...)` for automatic closing.
- You can read entire files at once or iterate line-by-line.

### Example
```python
# Writing to a file
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Hello, this is Day 11!\n")
    f.write("Learning Python file handling is fun.\n")

# Reading from a file
with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# Appending to a file
with open("example.txt", "a", encoding="utf-8") as f:
    f.write("This line was added later.\n")
