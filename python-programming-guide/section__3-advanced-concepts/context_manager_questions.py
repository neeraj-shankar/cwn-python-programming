"""
1. **What is a context manager in Python, and when would you use one?**

2. **Can you explain the `with` statement and its relationship with context managers?**

3. **How do you create a context manager using a class? What methods must be implemented?**

4. **Describe how you would use the `contextlib` module to create a context manager.**

5. **Can you provide an example of a context manager you've written to handle database transactions?**

6. **What are the `__enter__` and `__exit__` methods, and how are they used in a context manager?**

7. **How does a context manager handle exceptions that occur inside the `with` block?**

8. **Can you write a context manager that suppresses only specific exceptions? How would you test it?**

9. **Explain the difference between using a context manager and using a try/finally block. Are there any advantages to using one over the other?**

10. **How would you implement a thread-safe context manager for managing access to a shared resource?**

11. **What is the purpose of the `contextlib.ExitStack` class, and how would you use it?**

12. **Can you create a context manager that measures the execution time of a block of code?**

13. **How would you write a context manager that temporarily changes the current working directory in a program, and then restores it?**

14. **Discuss a scenario where you would use a nested `with` statement.**

15. **Can you explain how context managers can be used for resource pooling, such as reusing database connections?**

16. **How can you use a context manager to ensure that multiple files are closed properly after processing them?**

17. **What are some common use cases for context managers in Python standard libraries?**

18. **How would you debug an issue within a context manager?**

19. **Can you describe a real-world problem you solved using a custom context manager?**

20. **How would you extend a context manager to support asynchronous operations with `async with`?**

"""

class FileManager:
    
    def __init__(self, filepath, mode) -> None:
        self.filepath = filepath
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filepath, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exec_value, traceback):
        if exc_type is FileNotFoundError:
            print("File not found error was raised")

        if self.file:
            self.file.close()

    

with FileManager("redme.txt", 'r') as file:

    print(file.readline())


