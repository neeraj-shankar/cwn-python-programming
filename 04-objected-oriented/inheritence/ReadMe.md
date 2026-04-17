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

## Mixin
- In Python, a Mixin is a specialized type of multiple inheritance. It’s a class that provides a "bundle" of functionality to other classes but isn't meant to stand on its own.

### Key Characteristics
1. **No State:** Mixins typically don't have their own `__init__` methods or store data. They just provide methods.

2. **Not Standalone:** You shouldn't instantiate a Mixin directly. `my_mixin = MyMixin()` usually wouldn't make sense.

3. **Modular:** They allow you to share code across unrelated classes without a deep, messy inheritance tree.

```python
class FlyableMixin:
    def fly(self):
        print(f"{self.__class__.__name__} is soaring through the sky!")

class Bird(FlyableMixin):
    def eat(self):
        print("Eating seeds.")

class Airplane(FlyableMixin):
    def fuel_up(self):
        print("Taking on jet fuel.")

# Usage
sparrow = Bird()
boeing = Airplane()

sparrow.fly()  # Output: Bird is soaring through the sky!
boeing.fly()   # Output: Airplane is soaring through the sky!
```

### Tabular comparison between Standard Inheritence and Mixin
| Feature           | Standard Inheritance              | Mixin                                     |
| ----------------- | --------------------------------- | ----------------------------------------- |
| **Relationship**  | "Is a" (A Dog is an Animal)       | "Has a" / "Can do" (A Dog can talk)       |
| **Purpose**       | Defining a core hierarchy         | Adding optional/reusable features         |
| **State**         | Often stores data/attributes      | Usually only contains methods             |
| **Usage Style**   | Used for strong domain modeling   | Used for code reuse across classes        |
| **Dependency**    | Child tightly depends on parent   | Loosely coupled, can be combined flexibly |
| **Reusability**   | Limited (single hierarchy focus)  | High (can be mixed into multiple classes) |
| **Design Impact** | Deep hierarchies can become rigid | Promotes composition over inheritance     |
| **Example**       | `class Dog(Animal)`               | `class Dog(TalkMixin)`                    |

### Mixin and Composition
- Mixins and Composition are both used to solve the same problem: how to give a class new powers without creating a messy, deep inheritance tree.

#### The Core Difference
The easiest way to distinguish them is by looking at the relationship between the objects:

1. **Mixins use Inheritance ("is-a"):** A class becomes a type of that mixin. It absorbs the mixin’s methods directly into its own identity.

2. **Composition uses References ("has-a"):** A class holds an instance of another class. It delegates tasks to that internal object.

```python
# =======================================================================================
# ===================================  Mixin Approach ===================================
# =======================================================================================
class LoggerMixin:
    def log(self, message):
        print(f"[LOG]: {message}")

class Database(LoggerMixin):
    def save(self):
        self.log("Saving data...") # Direct access via 'self'

# =======================================================================================
# ==============================  Composition Approach ==================================
# =======================================================================================

class Logger:
    def log(self, message):
        print(f"[LOG]: {message}")

class Database:
    def __init__(self):
        self.logger = Logger() # The class 'has' a logger

    def save(self):
        self.logger.log("Saving data...") # Delegation

```