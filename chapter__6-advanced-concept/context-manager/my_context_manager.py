class MyContextManager:
    def __enter__(self):
        print("Entering the context")

    def __exit__(self, exc_type, exc_value, traceback):
        """

        :param: exc_type: This parameter holds the type of any exception that 
                          was raised within the context. If no exception was
                          raised, it will be None.

        :param exc_value: If an exception was raised, this parameter contains 
                          the exception object. If no exception occurred,
                          it will be None.

        :param traceback: This parameter holds a traceback object that provides
                          information about the call stack at the point where 
                          the exception was raised. If no exception occurred, 
                          it will be None.
        """
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