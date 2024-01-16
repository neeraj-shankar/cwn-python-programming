
What is context manager?
-----------------------------------------------------------------------------------------------------------------------
A context manager in Python is an object that defines the methods __enter__() and __exit__() which allow you to manage 
the setup and teardown of resources, such as files, network connections, and locks

Context managers are typically used with the with statement to ensure that resources are properly acquired and released.

When we use a context manager with the with statement, the resource (in this case, the file) is acquired 
when entering the block and automatically released when leaving the block.

