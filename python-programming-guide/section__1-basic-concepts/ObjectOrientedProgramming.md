# Object Oriented Programming in Python
- Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects," which can contain data in the form of fields (often known as attributes or properties) and code in the form of procedures (often known as methods).


## Key Concepts of OOPs

### Classes and Objects: 
- A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects (instances) will have. An object is an instance of a class.

### Encapsulation: 
- This principle states that all the internal representation of an object is hidden from the outside. 
- Only the object can interact with its internal data. Public methods are provided to allow controlled access to the object's properties.

### Inheritance: 
- This is a way to form new classes using classes that have already been defined. 
- The new class, known as a derived or child class, inherits attributes and methods from the base or parent class.

### Polymorphism: 
- This principle allows methods to do different things based on the object it is acting upon. 
- In other words, different objects can respond to the same method call in different ways.

### Abstraction: 
- Abstraction involves creating simple, more generalized representations of complex entities by highlighting what is important and omitting the irrelevant details.


## Classes and Objects

### Class:
- A class is a blueprint for creating objects. It defines a set of attributes that will characterize any object that is instantiated from this class. 


```sh
class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

```

### Objects:
- An object is an instance of a class. When the class is defined, no memory is allocated until an object is created.

```sh
dog1 = Dog("Buddy", 9)
dog2 = Dog("Fido", 3)

```

## Variable Types

### Instance Variables: 
- These are variables that are unique to each instance of a class. 
- They are defined within methods (usually within __init__) and are accessed using the self keyword. 
- They are used to store data that is specific to an object.

```sh
class Dog:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

```

### Class Variables: 
- Also known as static variables, these are shared across all instances of a class. 
- They are defined within the class but outside any instance methods. 
- Class variables are used for data that is common to all instances of the class.

```sh
class Dog:
    species = "Canis familiaris"  # Class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age

```


### Local Variables: 
- These are variables defined within a method and are only accessible within the scope of that method. 
- They are used for temporary storage that is not needed outside the method.

```sh
class Dog:
    def bark(self):
        sound = "Woof!"  # Local variable
        return sound
```

## Functions Types

### Instance Methods: 
- These are functions defined inside a class that operate on an instance of the class. 
- They must accept self as their first parameter, which represents the instance on which the method is being called. 
- Instance methods can access and modify instance variables and call other instance methods.

```sh
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):  # Instance method
        return f"{self.name} says woof!"

```

### Class Methods: 
- These are methods that are bound to the class rather than its object. 
- They have access to the class state and can modify class variables. 
- Class methods must accept cls as their first parameter, which represents the class itself. 
- They are defined using the @classmethod decorator.

```sh
class Dog:
    count = 0  # Class variable

    def __init__(self, name):
        self.name = name
        Dog.count += 1

    @classmethod
    def get_dog_count(cls):  # Class method
        return cls.count

```

### Static Methods: 
- These are methods that do not require access to the instance (self) or the class (cls). 
- They are defined using the @staticmethod decorator and behave just like regular functions, but they belong to the class's namespace. 
- Static methods are used when some processing is related to the class but does not require the class or its instances to perform any action.

```sh
class Dog:
    @staticmethod
    def is_animal():  # Static method
        return True

```

### Special Methods: 

- Also known as magic or dunder methods, these are special built-in methods that have double underscores at the beginning and end of their names
- (e.g., __init__, __str__, __len__). 
- They are used to override or add functionality to built-in functions or operations. 
- For example, __init__ is used for object initialization, __str__ is used to define a human-readable representation of an object, and __len__ is used to define the behavior of the len() function for the class instances.

```sh
class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Dog named {self.name}"

```