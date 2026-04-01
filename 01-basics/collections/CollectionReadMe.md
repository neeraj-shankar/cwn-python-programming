# Collection Module - Python

The **`collections` module** in Python is a **built-in standard library** that provides **alternatives to Python’s general-purpose built-in containers** like `dict`, `list`, `set`, and `tuple`.

It offers **specialized container datatypes** that are more efficient or convenient for certain use cases.

---

## 📦 **Top Features of the `collections` Module**
---


### 🔧 Summary Table - Here are the most commonly used classes and tools provided by `collections`:

| Tool          | Description               | Use Case                                |
| ------------- | ------------------------- | --------------------------------------- |
| `namedtuple`  | Tuple with named fields   | Immutable records with attribute access |
| `deque`       | Double-ended queue        | Fast FIFO/LIFO operations               |
| `Counter`     | Count hashable items      | Word count, frequency analysis          |
| `OrderedDict` | Dict with order preserved | Order-sensitive mappings                |
| `defaultdict` | Dict with default factory | Cleaner code for missing keys           |
| `ChainMap`    | Combines multiple dicts   | Multi-scope lookups                     |

---

## Double-Ended Queue
- deque (pronounced "deck") stands for Double-Ended Queue.
- Allows fast appends and pops from both ends.
- Implemented as a doubly linked list, not a dynamic array like a list.
- More efficient than list for queue and stack operations.

---

### 📦 Creating a deque

```python
from collections import deque

d = deque([1, 2, 3])
print(d)  # deque([1, 2, 3])
```

---

### 🔁 Core Methods and Their Usage

| Method             | Description                                 | Example                   |
| ------------------ | ------------------------------------------- | ------------------------- |
| `append(x)`        | Add to **right end**                        | `d.append(4)`             |
| `appendleft(x)`    | Add to **left end**                         | `d.appendleft(0)`         |
| `pop()`            | Remove and return from **right end**        | `d.pop()`                 |
| `popleft()`        | Remove and return from **left end**         | `d.popleft()`             |
| `extend(iterable)` | Extend at **right end**                     | `d.extend([4, 5])`        |
| `extendleft(iter)` | Extend at **left end** (*in reverse order*) | `d.extendleft([0, -1])`   |
| `rotate(n)`        | Rotate elements right (`+n`) or left (`-n`) | `d.rotate(1)` → `[3,1,2]` |
| `clear()`          | Remove all elements                         | `d.clear()`               |
| `reverse()`        | Reverse elements **in-place**               | `d.reverse()`             |

---

### ⏱️ Time Complexity

| Operation      | Time Complexity |
| -------------- | --------------- |
| `append()`     | O(1)            |
| `appendleft()` | O(1)            |
| `pop()`        | O(1)            |
| `popleft()`    | O(1)            |
| `insert(i, x)` | ❌ Not supported |
| Index access   | O(n)            |

> 🧠 `deque` is optimized for **fast insert/remove**, not for **index-based access**.

---

### 🎯 Use Cases of `deque`

1. **Queue Implementation** (FIFO):

```python
q = deque()
q.append('task1')
q.append('task2')
print(q.popleft())  # task1
```

2. **Stack Implementation** (LIFO):

```python
stack = deque()
stack.append('item1')
stack.append('item2')
print(stack.pop())  # item2
```

3. **Sliding Window / Fixed-Size Queue**:

```python
d = deque(maxlen=3)
d.extend([1, 2, 3])
d.append(4)  # Automatically drops 1
print(d)     # deque([2, 3, 4], maxlen=3)
```

4. **Palindrome Checker**:

```python
def is_palindrome(s):
    d = deque(s)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True
```

---

## 📌 Differences vs List

| Feature        | `deque`       | `list`         |
| -------------- | ------------- | -------------- |
| Append         | O(1)          | Amortized O(1) |
| Appendleft     | ✅ O(1)        | ❌ O(n)         |
| Pop from left  | ✅ O(1)        | ❌ O(n)         |
| Index access   | ❌ O(n)        | ✅ O(1)         |
| Insert at ends | ✅ Efficient   | ❌ Slower       |
| Use case       | Queues/stacks | Random access  |


## What is namedtuple?
A namedtuple is a lightweight object type from the collections module that lets you create tuple-like objects with named fields.
```python
from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'marks'])

s1 = Student('Neeraj', 21, 95)

print(s1.name)   # Neeraj
print(s1[1])     # 21 (still works like tuple)
```

### Benefits of namedtuple
- Access via names instead of indices Makes code self-documenting
- **Lightweight** (Better than class). Compared to a normal class: No **`__init__`** boilerplate, Less memory usage, Faster to create.
- Immutable (Like tuple). Once created, values cannot be changed

### Named Tuple vs Data class
| Feature     | namedtuple  | dataclass       |
| ----------- | ----------- | --------------- |
| Mutability  | ❌ Immutable | ✅ Mutable       |
| Performance | ⚡ Faster    | Slightly slower |
| Methods     | ❌ No        | ✅ Yes           |
| Defaults    | Limited     | ✅ Easy          |
| Use case    | Simple data | Rich objects    |
