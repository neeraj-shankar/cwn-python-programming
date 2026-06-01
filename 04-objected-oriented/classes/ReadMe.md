# Classes in Python World

## Meta Class
- A metaclass in Python is a class that defines how other classes are **created** and **behaves**, commonly used in frameworks to enforce rules, register classes, or modify class definitions at creation time.

```python
obj = MyClass()

# obj is an instance
# MyClass is a class
# Who creates MyClass? → A metaclass
```
- **Note**: Metaclass = class that creates classes. By default, all classes in Python are created by type

## The Class: The Blueprint
Think of a Class as a master plan or a stencil. It doesn't "do" anything on its own; it just defines what something is and what it can do.

- It’s a template that groups data (attributes) and behaviors (methods) together.

    - **Attributes:** The data or characteristics (e.g., color, height, brand).
    - **Methods:** The actions or functions (e.g., run, stop, calculate).

## The Object: The Instance
An Object is the actual thing you build using that blueprint. If "Car" is the class, then your specific shiny red Ferrari parked in the driveway is the object. This process of creating an object from a class is called **instantiation**.

## Exploring the Specifics

### The Constructor (`init`)
- When you create an object, you usually need to set its initial state. This is done via a Constructor. 
- It’s a special method that runs automatically the moment an object is born. 
- It’s like the factory settings for your new device.

### The "Self" (or this)
You’ll often see a keyword like `self` (Python) or `this` (Java/C++). This is how an object refers to itself.

## Object Oriented Concepts

### Encapsulation
- If Metaclasses are the "God Mode" of Python, Encapsulation is the "Security Guard."
- In most languages like Java or C++, encapsulation is enforced with rigid keywords like `public`, `private`, and `protected`. But Python follows the philosophy: **"We are all consenting adults here."** 
- Python doesn't physically lock doors; it just puts up "No Trespassing" signs and expects you to respect them.

#### The Three Levels of Access
1. **public:** Accessible from anywhere. No restrictions.
2. **Protected:** "Please don't touch this unless you're a subclass." (A hint/convention). eg- (`_name`)
3. **Private:** "Keep out!" Python will actually scramble the name to make it harder to find. Eg- (__name__)

#### The "Private" Mystery (Name Mangling)
When you use a double underscore (__), Python performs Name Mangling. It changes the attribute name internally so that a simple call to it fails. This prevents subclasses from accidentally overriding it.

```python
class SecretVault:
    def __init__(self):
        self.__passcode = "1234"

vault = SecretVault()
# print(vault.__passcode) # This throws an AttributeError!
print(vault._SecretVault__passcode) # Output: 1234 (The secret door is revealed!)
```
- Python renames it to `_ClassName__attributeName`.

#### The "Pythonic" Way: Properties
In other languages, you write `get_balance()` and `set_balance()`. In Python, we use the @property decorator. This allows you to keep an attribute **"private"** but access it like it's a normal variable

```python
class SmartAccount:
    def __init__(self):
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("You can't have a negative balance, buddy.")
        self.__balance = value

acc = SmartAccount()
acc.balance = 500  # Looks like a normal attribute, but triggers the setter!
# acc.balance = -10 # This would crash with our custom error.
```

### Polymorphism
The word literally means "many shapes." In programming, it’s the ability of different objects to respond to the same function call in their own specific way.

#### 1. The Real-World Analogy
Think of the "Play" button on your devices.
- On a YouTube app, "Play" starts a video.
- On a Spotify app, "Play" starts a song.
- On a Vinyl Player, "Play" drops a needle.

#### 2. Duck Typing: The Python Specialty
-  *"If it walks like a duck and quacks like a duck, then it’s a duck."*
- In Python, we don't care about the object's class; we only care about whether it has the method we’re trying to call.

```python
class Duck:
    def speak(self):
        return "Quack!"

class Dog:
    def speak(self):
        return "Woof!"

class Robot:
    def speak(self):
        return "Beep Boop!"

def make_it_talk(entity):
    # This function doesn't care what 'entity' is, 
    # as long as it has a .speak() method.
    print(entity.speak())

make_it_talk(Duck())  # Quack!
make_it_talk(Dog())   # Woof!
make_it_talk(Robot()) # Beep Boop!
```

#### 3. Polymorphism with Inheritance
- While Duck Typing is flexible, we often use Inheritance to ensure that different classes share the same "blueprint" (interface) via an Abstract Base Class (ABC). 
- This forces subclasses to implement specific methods.


## Dataclass

```python
from dataclasses import dataclass

class User:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        
        return f"User(name={self.name}, age={self.age})"

user = User("Neeraj", 20)

print(user)


@dataclass
class Student:
    name : str 
    agesss : str 
    

stu = Student("Neeraj", 23)
print(stu)
```