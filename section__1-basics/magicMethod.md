Magic methods in Python, also known as dunder methods (short for "double underscore"), are special methods that have double underscores at the beginning and the end of their names. They are used to provide custom implementations for built-in behavior in Python objects. These methods allow you to emulate the behavior of built-in types or to implement operator overloading.

Here are a few commonly used magic methods:

### `__init__(self, ...)`
This method is called when a new instance of a class is created. It's used for initializing the instance's attributes and for setting up any necessary state.

```python
class Example:
    def __init__(self, value):
        self.value = value
```

### `__str__(self)`
This method is called by the `str()` built-in function and by the `print()` function to obtain a human-readable string representation of an object.

```python
class Example:
    def __str__(self):
        return "Human-readable representation"
```

### `__repr__(self)`
This method is called by the `repr()` built-in function to obtain an official string representation of an object, which should ideally be a valid Python expression that could be used to recreate the object.

```python
class Example:
    def __repr__(self):
        return f"Example({self.value})"
```

### `__eq__(self, other)`
This method is called to implement the equality operator (`==`). It compares two objects for equality.

```python
class Example:
    def __eq__(self, other):
        return self.value == other.value
```

### `__lt__(self, other)`, `__le__(self, other)`, `__gt__(self, other)`, `__ge__(self, other)`
These methods are called to implement the less than (`<`), less than or equal to (`<=`), greater than (`>`), and greater than or equal to (`>=`) operators, respectively.

```python
class Example:
    def __lt__(self, other):
        return self.value < other.value
```

### `__add__(self, other)`
This method is called to implement the addition operator (`+`). It allows you to define how an instance of your class should behave when used with the `+` operator.

```python
class Example:
    def __add__(self, other):
        return Example(self.value + other.value)
```

### `__getitem__(self, key)`
This method is called to implement item access using the subscript notation (`obj[key]`).

```python
class Example:
    def __getitem__(self, key):
        return self.data[key]
```

### `__setitem__(self, key, value)`
This method is called to implement item assignment to the object using the subscript notation (`obj[key] = value`).

```python
class Example:
    def __setitem__(self, key, value):
        self.data[key] = value
```

### `__iter__(self)`
This method is called when an iterator is required for a container. It should return an object that implements the `__next__` method.

```python
class Example:
    def __iter__(self):
        return iter(self.data)
```

### `__next__(self)`
This method is called to implement the iterator protocol. It should return the next item in the sequence or raise `StopIteration` when there are no more items.

```python
class ExampleIterator:
    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
```

Magic methods enable you to define how objects behave with respect to the core Python syntax and built-in functions, making your custom objects more intuitive and integrated with the language.