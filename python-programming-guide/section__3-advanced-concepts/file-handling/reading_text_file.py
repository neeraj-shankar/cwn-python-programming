LINE_SEPARATOR = """
==================================================================================================="""

# Reading Text file
file = open("./test_file.txt", "r")

print(LINE_SEPARATOR)
print(f"File Content: {file} and Its Type: {type(file)}")

print(LINE_SEPARATOR)
content = file.read()  # reads the entire file content
print(content)

print(LINE_SEPARATOR)
line = file.readline()
print(f"First Line: {line}")

# Iterate each line using loop option
print(LINE_SEPARATOR)
print(f"The each line of the file: ")
for line in file:
    print(line)


# Reading text file using the context manager
# The with statement is a cleaner way to open and manage files. It automatically closes the file when the block is exited,
# even if an exception occurs.

try:
    with open("./test_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"File Not found")
