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

# FAQs

## 1. What is the difference between instance variables and class variables in OOP?

### Instance Variables
- **Scope:** Instance variables are specific to each instance of a class. This means that each object (instance) of the class has its own separate copy of instance variables.

- **Declaration:** They are usually declared within methods (typically within the __init__ method) and are prefixed with self in Python to denote that they belong to the object instance.

- **Usage:** Instance variables are used to store data that is unique to each object. For example, if you have a Dog class, each Dog object might have a different name and age, which would be stored as instance variables.

- **Lifetime:** The lifetime of instance variables is tied to the lifetime of the object instance. When the object is destroyed, the instance variables are also reclaimed by the system.

### Class Variables:

- **Scope:** Class variables are shared across all instances of a class. They are the same for every instance.

- **Declaration:** They are declared within the class body but outside any instance methods. In Python, class variables are not prefixed with self.

- **Usage:** Class variables are used to store data that is common to all instances of the class. For example, if all dogs of the Dog class are mammals, you might have a class variable species set to "mammal".

- **Lifetime:** The lifetime of class variables is tied to the lifetime of the class definition, not to any single object. They exist as long as the class exists in the runtime environment.

## Can you explain what a static variable is and when you would use it?

### Characteristics of Static Variables:
- **Shared Value:** The value of a static variable is shared across all instances of the class. If the value is changed in one instance, it changes for all instances.

- **Memory Efficiency:** Since there is only one copy of a static variable, regardless of how many instances of the class exist, it is more memory-efficient for data that is common to all instances.

- **Class-level Scope:** Static variables can be accessed directly through the class itself, without creating an instance of the class.

### When to Use Static Variables:

- **Common Property:** When a property is common to all instances of a class and should have the same value for each instance, a static variable is appropriate. For example, if all instances of a Person class should have the same species, you could use a static variable to store "Homo sapiens".

- **Configuration Data:** Static variables can be used to store configuration data that needs to be shared across all instances, such as application-wide settings.

- **Counting Instances:** If you need to keep track of the number of instances of a class that have been created, you can use a static variable as a counter that is incremented in the class constructor.

- **Utility Values:** Static variables can be used for values that are used by static methods, such as constants or lookup tables that are relevant to the class as a whole.

```sh
class Person:
    species = "Homo sapiens"  # Static (class) variable

    def __init__(self, name):
        self.name = name  # Instance variable

# Accessing the static variable without creating an instance
print(Person.species)  # Output: Homo sapiens

# Changing the static variable affects all instances
Person.species = "Homo neanderthalensis"
print(Person.species)  # Output: Homo neanderthalensis

# All instances share the same static variable
person1 = Person("Alice")
person2 = Person("Bob")
print(person1.species)  # Output: Homo neanderthalensis
print(person2.species)  # Output: Homo neanderthalensis

```

## How would you make a variable private in a Python class, and why might you want to do this?

### Why Make a Variable Private?

- **Encapsulation:** Encapsulation is a core principle of OOP. It involves bundling the data with the methods that operate on that data. By making variables private, you can hide their values and prevent external interference and misuse.

- **Control Access:** By making a variable private, you can control access to its value through methods (getters and setters), which can include additional logic for validation, logging, or other purposes.

- **Reduce Dependency:** If other parts of your codebase rely on a variable, changes to that variable can have widespread implications. Making a variable private helps to reduce this dependency and allows you to change the implementation without affecting external code.

- **Maintain Integrity:** Private variables can be used to maintain the integrity of the internal state of the object by preventing external code from setting the variables to invalid or inconsistent values.

- **Implementation Details:** Private variables can be used to hide implementation details from the user, allowing the developer to change these details without affecting the users of the class.

### Making a variable private

- We can make a variable "private" by prefixing its name with two underscores (__). This triggers name mangling, where the interpreter changes the name of the variable in a way that makes it harder to access from outside the class.

```sh 
class MyClass:
    def __init__(self):
        self.__private_variable = "I am private"

    def get_private_variable(self):
        return self.__private_variable
```
- It is not truly private, as Python does not enforce strict encapsulation, but the double underscores signal that it is intended for internal use within the class only
- The name mangling converts __private_variable to _MyClass__private_variable, which can still be accessed if you know the mangled name, but this is strongly discouraged as it breaks encapsulation and the intended use of the variable.

### Accessing Private Variables

```sh
obj = MyClass()
print(obj._MyClass__private_variable)  # Accessing the private variable (not recommended)
```

## In the context of OOP, what is encapsulation, and how does it relate to the concept of private and public variables?

- **Encapsulation** is a fundamental concept in object-oriented programming (OOP) that refers to the bundling of data with the methods that operate on that data. It restricts direct access to some of an object's components, which is a means of preventing accidental interference and misuse of the internal workings of an object.

- **Encapsulation** is often achieved through the use of access modifiers, which control the visibility of class members (variables and methods)

### Public Variables:

- **Accessibility:** Public variables can be accessed from anywhere—inside the class, from its subclasses, and from other classes.

- **Usage:** They are intended to be directly accessible without any restrictions. This is suitable for properties that do not require any special behavior or validation upon being read or written.


### Private Variables:

- **Accessibility:** Private variables are intended to be accessed only within the class that defines them. They are not accessible directly from outside the class.

- **Usage:** They are used to hide the internal state of an object from the outside. This is useful when you need to validate data before setting a value or if changing the value directly could leave the object in an inconsistent state.

### Encapsulation in Practice:


- **Getter and Setter Methods:** Encapsulation is often implemented using getter and setter methods (also known as accessors and mutators). These methods allow for controlled access to private variables. The getter method returns the value of the private variable, and the setter method allows you to set the value while potentially enforcing some constraints or triggering side effects.

- **Data Hiding:** Encapsulation is a form of data hiding. By making variables private, you hide their values and prevent external code from directly modifying them. This allows the internal representation of the object to be changed without affecting external code that relies on the object.

- **Controlled Access:** Encapsulation provides a controlled interface to the internal workings of the class. This means that you can change the internal implementation without changing how the class is used by other code.

```sh 
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):  # Getter method
        return self.__balance
```

## What is an instance method, and how does it differ from a static method in a class?

### Binding:

- **Instance** methods are bound to an instance of the class and can access and modify the object's state.

- **Static** methods are bound to the class itself and cannot access or modify instance-specific data.

### Parameters:

- **Instance** methods automatically take self as the first parameter, which refers to the instance calling the method.

- **Static** methods do not take self or any other instance-specific parameters.

## Usage:

- **Instance** methods are used when you need to access or modify the state of a particular object.

- **Static** methods are used when you need a function that is logically related to the class but does not need to access or modify the class or its instances.

### Calling:

- **Instance** methods are called on an instance of the class: instance.instance_method().

- **Static** methods can be called on the class itself or on an instance, but they behave the same way in both cases: MyClass.static_method() or instance.static_method().

### Decorator:

- **Instance** methods do not require any special decorator.

- **Static** methods require the @staticmethod decorator to indicate that they do not depend on the state of an instance.
