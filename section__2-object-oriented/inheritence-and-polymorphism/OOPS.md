# Object Oriented Programming in Python

## What is inheritance in python?

- It is a mechanism that allows you to create a hierarchy of classes that share a set of properties and methods by deriving a class from another class. 
- Inheritance is the capability of one class to derive or inherit the properties from another class.

### Benefits of inheritance are:
1. It represents real-world relationships well.
2. It provides the re-usability of a code. Also, it allows us to add more features to a class without modifying it.
3. It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B
   would automatically inherit from class A.
4. Inheritance offers a simple, understandable model structure. Less development and maintenance expenses result
   from an inheritance.


```python
# A Python program to demonstrate inheritance
class Person(object):

  # Constructor
  def __init__(self, name, id):
    self.name = name
    self.id = id

  # To check if this person is an employee
  def Display(self):
    print(self.name, self.id)

# Driver code
emp = Person("Satyam", 102) # An Object of Person
emp.Display()

Creating a Child Class
-------------------------------------------------------
class Emp(Person):

  def Print(self):
    print("Emp class called")

Emp_details = Emp("Mayank", 103)

# calling parent class function
Emp_details.Display()

# Calling child class function
Emp_details.Print()
```


### What is an object class in Python?
- Like the Java Object class, in Python (from version 3. x), the object is the root of all classes

    1. In Python 3.x, “class Test(object)” and “class Test” are same.
    2. In Python 2. x, “class Test(object)” creates a class with the object as a parent (called a new-style class), and
       “class Test” creates an old-style class (without an objecting parent).

### Subclassing (Calling constructor of parent class)
- In Python, every class inherits from a built-in basic class called ‘object’. The constructor i.e. the ‘__init__’ function of a class is invoked when we create an object variable or an instance of the class.

- The variables defined within __init__() are called instance variables or objects.

### The super() Function
- The super() function is a built-in function that returns the objects that represent the parent class.
- It allows to access the parent class’s methods and attributes in the child class.

## Different types of Python Inheritance
There are 5 different types of inheritance in Python. They are as follows:

1. **Single inheritance:** When a child class inherits from only one parent class, it is called single inheritance.
2. **Multiple inheritances:** When a child class inherits from multiple parent classes, it is called multiple inheritances.
3. **Multilevel inheritance:** When we have a child and grandchild relationship. This means that a child class will inherit from its parent class, which in turn is inheriting from its parent class.
4. **Hierarchical inheritance:** More than one derived class can be created from a single base.
5. **Hybrid inheritance:** This form combines more than one form of inheritance. Basically, it is a blend of more than one type of inheritance.

## The Diamond Problem

The **diamond problem** is a common issue in object-oriented programming when a class inherits from two classes that share a common ancestor. The problem arises because it can be unclear which method or attribute should be invoked from the shared ancestor class.

---

### **Understanding the Diamond Problem**

Consider this inheritance structure:

```css
      A
     / \
    B   C
     \ /
      D
```

Here:

- Class `A` is the root class.
- Classes `B` and `C` inherit from `A`.
- Class `D` inherits from both `B` and `C`.

The problem occurs if class `D` tries to access a method or attribute from `A`. Which version of `A`'s method should be used? The one inherited via `B` or via `C`? This ambiguity is the **diamond problem**.

---

### **How Python Handles the Diamond Problem**

Python uses the **C3 Linearization (Method Resolution Order)** to address this issue. The C3 linearization provides a deterministic order in which classes are searched for methods and attributes. This is also known as the **MRO (Method Resolution Order)**.

1. **MRO Algorithm**:
   - Start with the current class.
   - Search the parent classes in depth-first, left-to-right order.
   - Ensure each class is only visited once, and the order respects the inheritance hierarchy.

2. **Example**:
   ```python
   class A:
       def greet(self):
           print("Hello from A")

   class B(A):
       def greet(self):
           print("Hello from B")

   class C(A):
       def greet(self):
           print("Hello from C")

   class D(B, C):
       pass

   obj = D()
   obj.greet()
   ```

   **Output**:
   ```
   Hello from B
   ```

   **Explanation**:
   - The MRO for `D` is: `D -> B -> C -> A`.
   - The `greet` method is found in `B` first, so it is executed.

3. **Viewing MRO**:
   You can view the MRO of a class using:
   ```python
   print(D.mro())
   ```
   **Output**:
   ```
   [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
   ```

---

### **Key Points About Python’s Solution**
1. **Deterministic Resolution**:
   - Python resolves the ambiguity deterministically using the MRO, so there's no confusion about which method will be invoked.

2. **`super()` Integration**:
   - Python’s `super()` function works in line with the MRO.
   - It ensures that the next method in the MRO is called, even in a multiple inheritance setup.
   - Example:
     ```python
     class A:
         def greet(self):
             print("Hello from A")

     class B(A):
         def greet(self):
             print("Hello from B")
             super().greet()

     class C(A):
         def greet(self):
             print("Hello from C")
             super().greet()

     class D(B, C):
         def greet(self):
             print("Hello from D")
             super().greet()

     obj = D()
     obj.greet()
     ```

     **Output**:
     ```
     Hello from D
     Hello from B
     Hello from C
     Hello from A
     ```

     **Explanation**:
     - `super()` follows the MRO and ensures each class's method is called exactly once in the correct order.

---

### **Comparison with Other Languages**
- **C++**:
  - Requires explicit calls to the parent class to avoid ambiguity.
  - You need to specify `B::method()` or `C::method()` in `D`.

- **Java**:
  - Java does not support multiple inheritance of classes (only interfaces) to sidestep the diamond problem entirely.

---

### **Conclusion**
Python elegantly solves the diamond problem through the C3 Linearization (MRO). It ensures that the inheritance hierarchy is resolved in a consistent and predictable manner, avoiding ambiguity and promoting code clarity.