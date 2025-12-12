# Python Basics -- List and Tuples

---

## 🔸 1. **List in Python**

A **list** is a mutable, ordered collection of items that can hold elements of different data types.

### ✅ **Basic Syntax:**

```python
my_list = [1, 2, 3, "apple", True]
```

#### ✅ **Key Features:**

* Ordered
* Mutable (can be modified)
* Allows duplicate elements
* Can contain mixed data types (int, str, bool, etc.)


## 🔹 2. **Tuple in Python**

A **tuple** is an immutable, ordered collection of elements.

### ✅ **Basic Syntax:**

```python
my_tuple = (1, 2, 3, "apple", True)
```

> ✅ You can also create a tuple with a single element like: `single = (5,)` (Note the comma!)

### ✅ **Key Features:**

* Ordered
* **Immutable** (cannot be changed after creation)
* Allows duplicate elements
* Can contain mixed data types

Great idea! Adding **space and time complexity** to the operations table gives a deeper understanding, especially for performance-critical scenarios.

---

## ✅ **Python List – Common Operations with Complexity**

| Operation       | Syntax / Example       | Description                              | Time Complexity | Space Complexity |
| --------------- | ---------------------- | ---------------------------------------- | --------------- | ---------------- |
| Access by Index | `my_list[i]`           | Returns element at index `i`             | O(1)            | O(1)             |
| Append          | `my_list.append(x)`    | Adds `x` at the end                      | Amortized O(1)  | O(1)             |
| Insert          | `my_list.insert(i, x)` | Inserts `x` at index `i`                 | O(n)            | O(1)             |
| Remove by Value | `my_list.remove(x)`    | Removes first occurrence of `x`          | O(n)            | O(1)             |
| Pop (end)       | `my_list.pop()`        | Removes and returns last element         | O(1)            | O(1)             |
| Pop (i)         | `my_list.pop(i)`       | Removes and returns element at index `i` | O(n)            | O(1)             |
| Slice           | `my_list[a:b]`         | Returns a new list of elements           | O(b - a)        | O(b - a)         |
| Search (in)     | `x in my_list`         | Checks membership                        | O(n)            | O(1)             |
| Sort            | `my_list.sort()`       | Sorts list in place                      | O(n log n)      | O(1)             |
| Reverse         | `my_list.reverse()`    | Reverses list in place                   | O(n)            | O(1)             |
| Length          | `len(my_list)`         | Returns number of items                  | O(1)            | O(1)             |

---

## ✅ **Python Tuple – Common Operations with Complexity**

| Operation       | Syntax / Example    | Description                      | Time Complexity | Space Complexity |
| --------------- | ------------------- | -------------------------------- | --------------- | ---------------- |
| Access by Index | `my_tuple[i]`       | Returns element at index `i`     | O(1)            | O(1)             |
| Count           | `my_tuple.count(x)` | Number of times `x` occurs       | O(n)            | O(1)             |
| Index           | `my_tuple.index(x)` | Index of first occurrence of `x` | O(n)            | O(1)             |
| Slice           | `my_tuple[a:b]`     | Returns a new tuple              | O(b - a)        | O(b - a)         |
| Search (in)     | `x in my_tuple`     | Checks membership                | O(n)            | O(1)             |
| Length          | `len(my_tuple)`     | Returns number of items          | O(1)            | O(1)             |

---

### 🧠 Notes on Space Complexity:

* **Lists** are dynamic arrays. When appending, Python may allocate extra space (overallocation) to optimize performance — this affects real-world space usage.
* **Tuples** are more space-efficient than lists for the same number of elements because they are immutable and don’t require memory for dynamic resizing.

---

## FAQs

Certainly! Here’s a curated list of **interview questions on lists and tuples in Python**, specifically tailored for someone with **5 years of experience**. These range from basics to deeper performance and real-world application knowledge.

---

### 🔹 **Python Lists – Interview Questions**

#### ✅ *Conceptual & Behavioral*

1. **What are the differences between a list and an array in Python? When would you use one over the other?**
2. **Why is Python's list considered a dynamic array?**
3. **How does list resizing work internally?**
4. **What are the implications of list mutability in multithreaded applications?**

#### ✅ *Code-Based*

5. **Write a function to remove duplicates from a list while maintaining order.**
6. **Given a list of numbers, find all unique pairs that sum to a specific target.**
7. **How would you flatten a nested list structure like `[[1, 2], [3, [4, 5]], 6]` recursively?**
8. **Explain the difference between shallow copy and deep copy in the context of lists. Demonstrate with code.**
9. **How would you implement a queue using Python lists? What are the time complexity pitfalls?**

#### ✅ *Performance & Complexity*

10. **What is the time complexity of various list operations like `append()`, `insert()`, `remove()` and `sort()`?**
11. **Why is popping from the front of a list an O(n) operation? How would you improve that?**
12. **When would you use `collections.deque` instead of a list?**

---

### 🔹 **Python Tuples – Interview Questions**

#### ✅ *Conceptual*

13. **Why are tuples immutable, and how does that affect their performance and usability?**
14. **Can you explain the memory layout difference between a list and a tuple?**
15. **How does tuple packing and unpacking work in Python? Provide examples.**
16. **When would you choose a tuple over a list in real-world projects?**

#### ✅ *Code-Based*

17. **How would you swap two variables in Python using tuple unpacking?**
18. **Write a function that accepts variable-length arguments using `*args` and returns the longest tuple argument.**
19. **Can you write a function that returns multiple values and uses tuple unpacking to capture them?**

#### ✅ *Advanced Scenarios*

20. **How are tuples used as dictionary keys or in sets? Why can’t lists be used the same way?**
21. **Explain what happens under the hood when slicing a tuple. Is it a deep or shallow operation?**

---

### 🧠 Bonus (Lists vs Tuples)

22. **How would you benchmark the performance difference between lists and tuples?**
23. **Describe a use case in your past projects where using a tuple improved performance or reduced bugs.**
24. **Are tuples truly immutable if they contain mutable objects? Explain with examples.**

---
