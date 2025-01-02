from file_manager import FileManager

with FileManager("/Users/codewithneeraj/StudyZone/cwn-python-programming/section__3-advanced/context_manager/sample.txt", "a+") as file:
    file.write(f"I am the first line that is written..")
