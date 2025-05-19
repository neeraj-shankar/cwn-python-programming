"""
Simple python program to demonstrate method overriding
"""


class Computer:

    def __init__(self, computer_name):
        self.name = computer_name

    # demonstrate method overriding using default arguments
    def run_software(self, software_name):
        print(f" The computer named {self.name} is running the software --> {software_name}")


class Laptop(Computer):
    pass


"""

"""
lap1 = Laptop("Hp Laptop")

#  Making call using the object name
lap1.run_software("Microsoft Office")

# Making call using the class name
Laptop.run_software(lap1, "Pycharm Code editor")

# Making call to parent class
Computer.run_software(lap1, "VS Code editor")




