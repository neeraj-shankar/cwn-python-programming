# 

## Significance of `__name__`
- Python has a built-in variable called `__name__`. Every time you run a Python file, the interpreter sets this variable automatically:

- If you run the script directly: Python sets `__name__` to the string "__main__".

- If you import the script: (e.g., import my_script), Python sets `__name__` to the actual filename (e.g., "my_script").