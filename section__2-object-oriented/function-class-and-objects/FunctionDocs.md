# Classes and functions in Python

## Variables
-----------------------------------------------------------------------------------------------------------------------
In Python, class and instance variables are used to store data within classes, but they have different scopes and
purposes.

### Class Variables
1. Class variables are shared among all instances of a class.
2. They are defined within the class but outside of any instance methods.
3. Class variables are accessed using the class name or an instance of the class.
4. Changes to a class variable are reflected in all instances of the class.
5. They are often used to store constants or shared data among instances.


```python
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
```

## What are the different methods that can be used
In Python, there are three types of methods that you can define within a class: class methods, instance methods, and
static methods. Each type of method has different characteristics and use cases.

### Instance Method
1. **Instance methods** are the most common type of methods in Python classes.
2. They operate on instances of the class and have access to instance-specific data and attributes.
3. The first parameter of an instance method is conventionally named self, which refers to the instance itself.
4. Instance methods can access and modify instance variables.
5. They can also call other instance methods and access class variables.

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def instance_method(self):
        return f"Instance method called with value: {self.value}"

# Creating an instance
obj = MyClass(42)

# Calling an instance method
result = obj.instance_method()
print(result)  # Output: "Instance method called with value: 42"

```

### Class Methods
1. **Class methods** are defined using the *@classmethod* decorator.
2. They operate on the class itself rather than on instances.
3. The first parameter of a class method is conventionally named cls, which refers to the class.
4. Class methods can access and modify class variables, but they cannot access instance-specific data.
5. They are often used for factory methods or operations that affect the entire class.

```python
class MyClass:
    class_variable = 10

    def __init__(self, value):
        self.value = value

    @classmethod
    def class_method(cls):
        return f"Class variable value: {cls.class_variable}"

# Creating an instance
obj = MyClass(42)

# Calling a class method
result = MyClass.class_method()
print(result)  # Output: "Class variable value: 10"
```

### Static Method
1. Static methods are defined using the *@staticmethod* decorator.
2. They are not bound to the class or its instances and do not have access to instance or class variables.
3. They behave like regular functions but are placed within the class's namespace for organization.
4. Static methods are often used for utility functions that are related to the class but don't require access to instance or class data.

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Calling a static method
result = MathUtils.add(3, 5)
print(result)  # Output: 8
```

## **method overriding** and **method overloading** in python
---

### **Method Overriding**
- **Definition**: When a subclass provides a specific implementation of a method already defined in its parent class.
- **Purpose**: Allows the subclass to modify or extend the behavior of the parent class's method.
- **Key Points**:
  - The method in the child class has the same name and parameters as the one in the parent class.
  - The method in the subclass **overrides** the parent class's method.
  - You can still access the parent class's method using `super()`.

#### **Example**:
```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")
        super().greet()  # Optional: Call the parent method

child = Child()
child.greet()
```

**Output**:
```
Hello from Child
Hello from Parent
```

#### **Use Case**:
- Specializing behavior for a subclass while retaining base functionality.
- Example: A `Shape` class with a `draw` method that is overridden by specific shapes like `Circle` and `Square`.

---

### **Method Overloading**
- **Definition**: Having multiple methods with the same name but different numbers or types of parameters.
- **Purpose**: Allows different behaviors based on arguments provided.
- **Key Points**:
  - **Python does not support traditional method overloading** (like Java or C++) because functions in Python can be redefined.
  - Instead, you can achieve a similar effect using **default arguments** or variable-length arguments (`*args` and `**kwargs`).

#### **Example Using Default Arguments**:
```python
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5))          # Output: 5
print(calc.add(5, 10))      # Output: 15
print(calc.add(5, 10, 15))  # Output: 30
```

#### **Example Using `*args`**:
```python
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(5))             # Output: 5
print(calc.add(5, 10))         # Output: 15
print(calc.add(5, 10, 15, 20)) # Output: 50
```

---

### **Comparison**

| Feature              | **Method Overriding**                   | **Method Overloading**                       |
|----------------------|------------------------------------------|---------------------------------------------|
| **Purpose**          | Modify or extend a parent's method.     | Define methods with varying arguments.      |
| **Context**          | Happens in inheritance (parent-child).  | Happens in the same class.                  |
| **Flexibility**      | Explicitly replaces base behavior.      | Adds flexibility to a single method.        |
| **Python Support**   | Fully supported with `super()`.         | Achieved using default arguments or `*args`.|
| **Example**          | Redefining `greet` in a child class.    | Adding numbers with varying arguments.      |

---

### **When to Use Each**
- Use **overriding** when you need to tailor a method’s behavior in a subclass to reflect its specific role.
- Use **overloading** when you want a method to handle multiple cases, such as different numbers or types of arguments, for convenience and code readability.

