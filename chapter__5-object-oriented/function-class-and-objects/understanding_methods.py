"""
Understanding the instance methods
"""


class MyClass:

    def __init__(self, value):
        self.value = value

    def instance_method(self):
        print(f"Instance method called with value--> {self.value}")


"""
Creating instance and calling instance method
"""
obj = MyClass(34)
obj.instance_method()

"""
Understanding the class method and its implementation
"""


class DemonstrateClassMethod:

    class_variable = 10

    def __int__(self, value):
        self.value = value

    @classmethod
    def class_method(cls):
        print(f"Class Variable Value --> {cls.class_variable}")


"""
Calling the class method
"""
DemonstrateClassMethod.class_method()

"""
Understanding the implementation of static method
"""


class DemonstrateStaticMethod:
    class_variable = 12

    def __int__(self, value):
        self.value = value

    @staticmethod
    def static_method(a, b):
        print(f"The sum of the two numbers {a} and {b} is {a +b}")


"""
Calling the static method
"""
DemonstrateStaticMethod.static_method(12, 12)
