"""
Certainly! Here are some interview questions that focus on the types of methods and variables in object-oriented programming (OOP):

### Questions on Variables:
1. What is the difference between instance variables and class variables in OOP?
2. Can you explain what a static variable is and when you would use it?
3. How would you make a variable private in a Python class, and why might you want to do this?
4. In the context of OOP, what is encapsulation, and how does it relate to the concept of private and public variables?
5. Can you provide an example of when you might use a class variable instead of an instance variable?

### Questions on Methods:
6. What is an instance method, and how does it differ from a static method in a class?
7. Can you explain what a class method is and provide a use case for it?
8. How would you override a method in a subclass, and can you give an example?
9. What are magic methods in Python, and can you list a few commonly used ones?
10. Describe the `@staticmethod` and `@classmethod` decorators in Python. What do they do, and how do they change the behavior of a method?

### Questions on Both Variables and Methods:
11. How do you define a read-only property in a Python class?
12. What is the purpose of the `__init__` method in Python classes?
13. Can you explain the concept of polymorphism with an example related to methods?
14. How can you prevent a method from being overridden in a subclass?
15. What is the significance of the `self` keyword in Python class methods?

### Scenario-Based Questions:
16. Imagine you have a base class `Animal` and subclasses `Dog` and `Cat`. How would you design the classes so that each subclass has a unique method to make a sound?
17. How would you implement a counter that keeps track of the number of instances created for a particular class?
18. If you have a method that doesn't access any properties of the class, should it be an instance method, a class method, or a static method? Why?
19. Describe a situation where you would use inheritance, and explain how class and instance variables might be involved.
20. How can you use property decorators (`@property`, `@setter`, and `@deleter`) to control access to class attributes?

"""

# Can you provide an example of when you might use a class variable instead of an instance variable?

# Example: Counting Instances of a Class

class Product:

    """
    Suppose you want to keep track of how many instances of a class have been created. This is a perfect use case for
    a class variable because the count is not specific to any single instance but is a property of the class as a whole.
    """
    # Class variable to count the number of instances
    instance_count = 0

    def __init__(self, name, price):
        self.name = name  # Instance variable
        self.price = price  # Instance variable
        # Increment the class variable for each new instance created
        Product.instance_count += 1

# Create instances of Product
product1 = Product("Chair", 49.99)
product2 = Product("Table", 89.99)
product3 = Product("Lamp", 24.99)
product4 = Product("Desk", 34.29)

# Access the class variable
print(f"Total number of Product instances: {Product.instance_count}")
# Output: Total number of Product instances: 4



# Example: Default Configuration
class Server:
    # Class variable for default timeout
    default_timeout = 30

    def __init__(self, ip_address, timeout=None):
        self.ip_address = ip_address  # Instance variable
        self.timeout = timeout if timeout is not None else Server.default_timeout

# Create a server instance with the default timeout
server1 = Server("192.168.1.1")

# Create a server instance with a custom timeout
server2 = Server("192.168.1.2", timeout=45)

# Access the instance variable
print(f"Server1 timeout: {server1.timeout}")  # Output: Server1 timeout: 30
print(f"Server2 timeout: {server2.timeout}")  # Output: Server2 timeout: 45
