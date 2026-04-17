# Interfaces and abtract classes in Python

## Interfaces
- Think of an interface as a contract. If a class "signs" the contract, it promises to implement specific methods. If it doesn't, Python won't even let you create an instance of that class.

### 1. The Core Concept: ABCs
To create an interface in Python, you use the abc module. You need two main components:

- **ABC:** The parent class your interface inherits from.
- **@abstractmethod:** A decorator that marks a method as "required."

#### The "Blueprint" Example#
- Imagine you're building a payment system. You want to make sure every payment method (Credit Card, PayPal, Bitcoin) has a process_payment method.

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        """All subclasses must implement this method!"""
        pass

    @abstractmethod
    def refund(self, transaction_id):
        pass
```

### 2. Implementing the Interface
- When a class inherits from your **PaymentProcessor**, it must define those **abstract methods**. If you forget one, Python raises a **TypeError**.

### Interfaces vs. Duck Typing
Python is famous for Duck Typing: "If it walks like a duck and quacks like a duck, it’s a duck." In many Python projects, developers don't use ABCs; they just assume the object has the method they need. However, as projects grow in complexity (or when you're working in a team), ABCs add a layer of formal structure that Duck Typing lacks.