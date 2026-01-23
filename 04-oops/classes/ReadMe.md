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