# Python - File Handling

This project introduces Python's input/output mechanisms with a focus on
file manipulation: opening, reading, writing and appending to text files,
while making sure file resources are always properly released.

## Learning Objectives

- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the `with` statement

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- First line of every file: `#!/usr/bin/env python3`
- All files end with a new line and are executable
- Code follows `pycodestyle` (version 2.7.*)
- No module imports allowed
- Every file operation uses the `with` statement

## Files

| File | Function | Description |
|------|----------|-------------|
| `read_file.py` | `read_file(filename="")` | Reads a UTF-8 text file and prints its content to stdout |
| `write_file.py` | `write_file(filename="", text="")` | Writes a string to a UTF-8 text file (creates it if needed, overwrites existing content) and returns the number of characters written |
| `append_write.py` | `append_write(filename="", text="")` | Appends a string to the end of a UTF-8 text file (creates it if needed) and returns the number of characters added |

## Usage

```python
#!/usr/bin/env python3
read_file = __import__('read_file').read_file
write_file = __import__('write_file').write_file
append_write = __import__('append_write').append_write

nb = write_file("my_file.txt", "Hello\n")
print(nb)                       # 6
nb = append_write("my_file.txt", "Holberton\n")
print(nb)                       # 10
read_file("my_file.txt")        # Hello
                                # Holberton
```

## Key Concepts

| Mode | Creates file if missing | Erases existing content | Cursor starts at |
|------|------------------------|-------------------------|------------------|
| `"r"` | No (raises `FileNotFoundError`) | No | Beginning |
| `"w"` | Yes | Yes | Beginning |
| `"a"` | Yes | No | End |

The `with` statement guarantees the file is closed automatically when the
block ends, even if an exception occurs.

## Author

Khaled Al-Yahya
