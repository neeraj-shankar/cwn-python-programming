"""
Python elegantly solves the diamond problem through the C3 Linearization (MRO). 
It ensures that the inheritance hierarchy is resolved in a consistent and predictable manner, 
avoiding ambiguity and promoting code clarity.
"""

class A:

    def greet(self):
        print("Hello from class A")

class B(A):

    def greet(self):
        print("Hello from class B")
        super().greet()

class C(A):

    def greet(self):
        print("Hello from class C")
        super().greet()

class D(B, C):
        pass

# Creating objects and function calls
d_object = D()
d_object.greet()
print(D.mro())