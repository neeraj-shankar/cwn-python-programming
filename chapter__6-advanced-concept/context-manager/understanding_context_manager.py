
class CustomFileManager:

    def __init__(self, filename, mode) -> None:
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Using context manager to write to an file
with CustomFileManager("sample.txt", "w") as file:
    file.writelines("Testing the context manager 2")
    print(f"Data written")

"""
The MyFileManager class defines __enter__() and __exit__() methods.
In the __enter__() method, it opens the file and returns it. This is the resource that you want to manage.
In the __exit__() method, it ensures the file is closed, regardless of whether an exception occurred.

When you use a context manager with the with statement, the resource (in this case, the file) is acquired 
when entering the block and automatically released when leaving the block.
"""

#######################################################################################################################
#
#######################################################################################################################

class MyContextManager:
    def __enter__(self):
        print("Entering the context")

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:  # An exception occurred
            print(f"Exception Type: {exc_type}")
            print(f"Exception Value: {exc_value}")
            print("Handling the exception")
        print("Exiting the context")

# Using the context manager
with MyContextManager():
    print("Inside the context")
    # Uncomment the next line to simulate an exception
    # raise ValueError("Something went wrong")
print("Outside the context")

"""
Here's an explanation of the parameters passed to the __exit__ method:

self: This parameter is the usual instance of the context manager class. It allows you to access instance variables and 
      methods within the context manager.

exc_type: This parameter holds the type of any exception that was raised within the context. If no exception was 
          raised, it will be None.

exc_value: If an exception was raised, this parameter contains the exception object. If no exception occurred, 
           it will be None.

traceback: This parameter holds a traceback object that provides information about the call stack at the point 
           where the exception was raised. If no exception occurred, it will be None.
"""
