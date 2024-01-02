""" 
It is a mechanism that allows you to create a hierarchy of classes that share a set of properties and methods by deriving a class from another class. 
Inheritance is the capability of one class to derive or inherit the properties from another class. 
"""

class Person:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display_person_detail(self):
        print(f"Person details from Parent Class: Name --> {self.name} and ID --> {self.id}")



class Employee(Person):

    def disply_employee_detail(self):

        print(f"If you have reached here. It means employee class is called. ")
    



""" 
The super() function is a built-in function that returns the objects that represent the parent class. 
It allows to access the parent class’s methods and attributes in the child class.
"""

class NameList:

    def __init__(self, name_list, sn_no):
        self.name_list = name_list
        self.sn_no = sn_no

    def show_list(self):
        print(f"The names of the student --> {self.name_list}")
        print(f"The roll number of students --> {self.sn_no}")

class StudentDetail(NameList):
    def __init__(self):
        print("Passing student list: ")
        super().__init__(["Neeraj", "Ayush", "Sanket"], [1, 2, 3])
        super().show_list()

    

""" 
Objects and functions calls
"""

# Create Object for person class and initialize the constructor with name and ID
obj = Person("Neeraj Shankar", "24")

# Making call to display method
obj.display_person_detail()

obj_child = Employee("Neeraj Ranjan", "23")
obj_child.disply_employee_detail()
obj_child.display_person_detail()


# Creating object of StudentDetail and making funtion calls
second_obj = StudentDetail()
