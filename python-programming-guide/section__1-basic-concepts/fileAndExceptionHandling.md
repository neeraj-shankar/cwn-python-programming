# Exception Handling in Python

## Overview
- Exception handling in Python is a mechanism that allows you to deal with runtime errors in a controlled and graceful manner. 
- It uses the **try**, **except**, **else**, and **finally** blocks to catch and handle exceptions.

## Here's a brief overview of each block:

### try:
- This block contains the code that might raise an exception. 
- If an exception occurs, the rest of the code in this block is skipped, and the except block is executed.

### except:
- This block catches and handles the exception. You can specify which exceptions you want to catch, or catch all exceptions. 
- Multiple except blocks can be used to handle different types of exceptions.

### else:
- This block is optional and is executed only if no exceptions were raised in the try block. 
- It's typically used for code that should run only if the try block was successful.

### finally:
- This block is optional and is executed no matter what, whether an exception was raised or not. 
- It's often used for cleanup actions, such as closing files or releasing resources.


## Some Common Exceptions that can happen while interacting with a file

### FileNotFoundError:
- Raised when a file or directory is requested but doesn't exist. This is common when trying to open a file for reading that doesn't exist.

### PermissionError:
- Raised when trying to perform a file operation without the adequate access rights. 
- This could happen when trying to read from or write to a file that you don't have permission to access

### IsADirectoryError:
- Raised when a file operation is requested on a directory. For example, this would occur if you try to open a directory as if it were a file.

### NotADirectoryError:
- Raised when a directory operation is requested on something that is not a directory. 
- For example, this would occur if you try to list the contents of a regular file as if it were a directory.

### IOError (or OSError in Python 3):
- Raised for input/output related errors, such as "file not found" or "disk full" errors. In Python 3, IOError is an alias for OSError, and specific subclasses like FileNotFoundError and PermissionError are used.


### EOFError: 
- Raised when one of the built-in functions (input() or raw_input()) hits an end-of-file condition (EOF) without reading any data. 
- This is less common with file operations but can occur in some contexts.

### BlockingIOError: 
- Raised when an operation would block on an object (e.g., file) set for non-blocking operation. 
- This is more common in non-blocking I/O operations.
    
### InterruptedError: 
- Raised when a system call is interrupted by an incoming signal.

### ValueError: 
- Raised when a function receives an argument of the correct type but with an inappropriate value, such as when passing an invalid mode to the open() function.

### UnicodeDecodeError: 
- Raised when reading a file in text mode with an encoding that doesn't match the file content.

### UnicodeEncodeError: 
- Raised when writing to a file in text mode with an encoding that cannot encode the output.

```sh 
BaseException
 └── Exception
      └── OSError
           ├── FileNotFoundError
           ├── PermissionError
           ├── IsADirectoryError
           ├── NotADirectoryError
           ├── BlockingIOError
           ├── InterruptedError
           └── ... (other OSError subclasses)
```

## Some Common Exceptions that can happen while interacting with dictionary, lists, tuple and set

### Dictionary Exceptions:

1. KeyError: Raised when trying to access a key that doesn't exist in the dictionary.
2. TypeError: Raised when using an unhashable type as a dictionary key, such as a list or another dictionary.


### List Exceptions:

1. IndexError: Raised when trying to access an index that is out of the range of the list.
2. ValueError: Raised when trying to remove a value from a list that does not exist.
3. TypeError: Raised when performing an operation on the list with an inappropriate type, such as concatenating a list with a non-iterable.


### Tuple Exceptions:

1. IndexError: Raised when trying to access an index that is out of the range of the tuple.
2. TypeError: Raised when trying to modify a tuple, which is an immutable data type.


### Set Exceptions:

1. KeyError: Raised when trying to remove an element from a set that does not exist.
3. TypeError: Raised when trying to add an unhashable type to a set, such as a list or another set.

# File Handling in Python

## Overview
-File handling in Python is a way to read from and write to files on the disk. 
- The built-in open() function is used to get a file object, which provides methods and attributes to interact with the file content.

``` sh
file_object = open('file.txt', 'r')  # Open for reading ('r' is the default mode)

```

### The mode argument can be:
The mode argument can be:

1. 'r': Read (default). Opens the file for reading.
2. 'w': Write. Opens the file for writing, creating it if it doesn't exist, or truncating it to zero length if it does.
3. 'a': Append. Opens the file for writing, creating it if it doesn't exist, without truncating it.
4. 'b': Binary. Opens the file in binary mode (e.g., 'rb' or 'wb').
5. '+': Update. Opens the file for both reading and writing.


### Reading a file

``` sh
# Read the entire file content
content = file_object.read()

# Read one line at a time
line = file_object.readline()

# Read all lines into a list
lines = file_object.readlines()
```

### Writing to a file

``` sh
# Write a string to the file
file_object.write('Hello, World!\n')

# Write a list of strings to the file
lines = ['First line\n', 'Second line\n']
file_object.writelines(lines)

```

### Using with Statement:
``` sh
try:
    with open('source.txt', 'r') as source_file:
        content = source_file.read()
    
    with open('destination.txt', 'w') as destination_file:
        destination_file.write(content)
except FileNotFoundError:
    print("The source file does not exist.")
except IOError:
    print("An I/O error occurred.")

```

