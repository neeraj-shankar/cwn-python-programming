##############################################################################
## Example: The CustomFileManager class defines __enter__() and __exit__()
## methods. In the __enter__() method, it opens the file and returns it.
## In the __exit__() method, it ensures the file is closed, regardless of
## whether an exception occurred.
##############################################################################


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
