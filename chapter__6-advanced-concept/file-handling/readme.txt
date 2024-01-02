About File Handling
-----------------------------------------------------------------------------------------------------------------------
You can open a file using the open() function. This function takes two arguments: the name of the file and the mode (read, write, or append).

Reading from a File
-----------------------------------------------------------
You can read the contents of a file using methods like read(), readline(), or by iterating through the file object.

Example
-----------------------------
content = file.read()  # Read the entire file content
line = file.readline()  # Read one line at a time
for line in file:  # Iterate through the lines
    print(line)


Exploring OS Module
-----------------------------------------------------------------------------------------------------------------------

File and Directory Operations:
-----------------------------------------------------------

os.getcwd()
-----------------------------
Get the current working directory.

os.chdir(path)
-----------------------------
Change the current working directory to the specified path.

os.listdir(path)
-----------------------------
List files and directories in the specified directory.

os.mkdir(path)
----------------------------
Create a new directory.

os.makedirs(path)
----------------------------
Create multiple directories, including parent directories if they don't exist.

os.rmdir(path)
----------------------------

os.remove(path)
----------------------------
Remove a file.

Path Manipulation:
-----------------------------------------------------------

os.path.join()
-----------------------------
Join one or more path components intelligently. It's useful for creating cross-platform paths.

os.path.abspath(path)
-----------------------------
Return the absolute version of a path.

os.path.basename(path)
-----------------------------
Get the base name of a path (i.e., the filename or the last directory).


os.path.dirname(path)
-----------------------------
 Get the directory name from a path.

File Information
-----------------------------------------------------------
os.path.exists(path)
-----------------------------
Check if a path exists.

os.path.isfile(path)
-----------------------------
Check if a path points to a file.

os.path.isdir(path)
-----------------------------
Check if a path points to a directory.

os.path.getsize(path)
-----------------------------
Get the size of a file in bytes.


File Permissions:
-----------------------------------------------------------

os.chmod(path, mode)
-----------------------------
Change the permissions of a file or directory.

os.stat(path)
-----------------------------
Get information about a file, including permissions and timestamps.


Environment Variables:
-----------------------------------------------------------
os.environ
-----------------------------
A dictionary containing the current environment variables.

Executing Shell Commands:
-----------------------------------------------------------
os.system(command)
-----------------------------
Run a shell command.

os.popen(command)
-----------------------------
Open a pipe to or from a shell command.



Miscellaneous
-----------------------------------------------------------
os.rename(src, dst)
-----------------------------
Rename a file or directory.

os.symlink(src, dst)
----------------------------
Create a symbolic link.

os.walk(top)
-----------------------------
Generate the file names in a directory tree by walking either top-down or bottom-up through the directory tree.


Error Handling:
-----------------------------------------------------------
os.error
-----------------------------
The base class for exceptions raised by the os module.















