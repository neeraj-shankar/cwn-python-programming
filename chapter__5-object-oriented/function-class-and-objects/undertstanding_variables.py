class MyClass:
    class_variable = 10  # This is a class variable

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable  # This is an instance variable


# Accessing class variable
print(MyClass.class_variable)  # Output: 10

# Creating instances
obj1 = MyClass(20)
obj2 = MyClass(30)

# Accessing instance variables
print(obj1.instance_variable)  # Output: 20
print(obj2.instance_variable)  # Output: 30

# Modifying class variable
MyClass.class_variable = 15
print(obj1.class_variable)  # Output: 15
print(obj2.class_variable)  # Output: 15