"""
Different types of exceptions in python:
--------------------------------------------
SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, 
             a missing colon, or an unbalanced parenthesis.

TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.

NameError: This exception is raised when a variable or function name is not found in the current scope.

IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.

KeyError: This exception is raised when a key is not found in a dictionary.

ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert
            a string to an integer when the string does not represent a valid integer.

AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent 
                attribute of a class instance.

IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.

ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.

ImportError: This exception is raised when an import statement fails to find or load a module.



Try with Else Clause
------------------------------
In Python, you can also use the else clause on the try-except block which must be present after all the except clauses. The code enters 
the else block only if the try clause does not raise an exception.


Advantages of Exception Handling:
----------------------------------
Improved program reliability: By handling exceptions properly, you can prevent your program from crashing or producing incorrect results due to 
                              unexpected errors or input.

Simplified error handling: Exception handling allows you to separate error handling code from the main program logic, making it easier to read and 
                           maintain your code.

Cleaner code: With exception handling, you can avoid using complex conditional statements to check for errors, leading to cleaner and more readable code.

Easier debugging: When an exception is raised, the Python interpreter prints a traceback that shows the exact location where the exception occurred, 
                  making it easier to debug your code.


Disadvantages of Exception Handling:
---------------------------------------

Performance overhead: Exception handling can be slower than using conditional statements to check for errors, as the interpreter has to perform additional 
                      work to catch and handle the exception.

Increased code complexity: Exception handling can make your code more complex, especially if you have to handle multiple types of exceptions or implement 
                           complex error handling logic.
                           
Possible security risks: Improperly handled exceptions can potentially reveal sensitive information or create security vulnerabilities in your code, 
                         so it’s important to handle exceptions carefully and avoid exposing too much information about your program.

"""