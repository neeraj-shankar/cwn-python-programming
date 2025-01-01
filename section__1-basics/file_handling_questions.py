"""

1. Explain the difference between the modes 'r+', 'w+', and 'a+' when opening a file in Python.

2. How do you read a specific line from a file in Python? For example, how would you read the 5th line from a file?

3. What is the difference between the read() and readlines() methods when working with file objects in Python?

4. How would you write a list of strings to a file in Python, with each string on a new line?

5. What is the purpose of the with statement when working with files in Python, and what advantage does it have over using open() and close() methods?

6. How can you ensure that a file is automatically closed after its contents have been processed, even if an error occurs during processing?

7. Describe how you would handle a situation where you need to read a large file in Python that cannot fit entirely in memory.

8. What is a file object in Python, and what are some common methods you can call on it?

9. How do you check if a file exists before attempting to read it in Python, and which exception is raised if you try to open a non-existent file?

10. Explain how you would handle different character encodings when reading and writing text files in Python. What issues might arise with encoding, and how can you prevent them?

"""
from itertools import islice


class FileHandlingPracticeSet:

    def __init__(self, file_path) -> None:
        self.path = file_path

    def understanding_different_modes(self):
        """
        Explore the different modes a file can be handled
        """

        # This opens file only in read mode. Cannot be over written or appended
        # my_file = open(self.path, "r")

        # This open in read and update mode. Any edit will be added at the end of file.
        # my_file = open(self.path, "r+")

        # This opens file in both read and write mode. The will be overwritten.
        # my_file = open(self.path, "w+")


        # This opens file in read and append mode. Any data written gets appended to end of file.

        my_file = open(self.path, 'a+')
        print(my_file.readline())
        my_file.write("This file is being written.")
        
        my_file.close()

    def read_specific_line_iterative(self, line_number):

        """
        Takes file path and line number and return the content of the line number requested.
        If requested line not found, returns None. 

        This method is memory-efficient and suitable for large files, as it doesn't require loading the entire file into memory.

        Returns: Line content if line number found else None
        """

        current_line = 1
        with open(self.path, 'r') as file:
            
            for line in file:
                if current_line == line_number:
                    return line
                current_line += 1
            return None
        
    
    def read_specific_line_itertools(self, line_number):

        with open(self.path, 'r') as file:

            line = next(islice(file, line_number-1, line_number), None)
            return line


if __name__ == "__main__":

    FILE_PATH = r'D:\Studyzone\cwn-python-programming\python-programming-guide\section__1-basic-concepts\test.txt'

    # Testing understanding_different_modes() method
    # FileHandlingPracticeSet(FILE_PATH).understanding_different_modes()

    # Testing read_specific_line_iterative() method
    line_number = 3
    line_text = FileHandlingPracticeSet(FILE_PATH).read_specific_line_iterative(line_number)
    print(f"Content at line number {line_number}: {line_text}")


    # Testing read_specific_line_iterative() method
    line_number = 4
    line_text = FileHandlingPracticeSet(FILE_PATH).read_specific_line_itertools(line_number)
    print(f"Content at line number {line_number}: {line_text}")



