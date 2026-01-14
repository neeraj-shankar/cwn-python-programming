# Comprensive Guide on Understanding and using list.

## 1. Adding Elements

### `append(element)`
**Purpose:** Add element to end of list

**Time Complexity:** O(1) amortized*  
**Space Complexity:** O(1)

```python
numbers = [1, 2, 3]
numbers.append(4)  # [1, 2, 3, 4]
```

*Amortized: Occasionally O(n) when list needs to resize, but averages to O(1)

---

### `extend(iterable)`
**Purpose:** Add all elements from iterable to end

**Time Complexity:** O(k) where k = length of iterable  
**Space Complexity:** O(k)

```python
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])  # [1, 2, 3, 4, 5, 6]
```

---

### `insert(index, element)`
**Purpose:** Add element at specific index

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

```python
numbers = [1, 2, 4]
numbers.insert(2, 3)  # [1, 2, 3, 4]
# Must shift all elements after index 2
```

**Why O(n)?** Must shift all elements to the right of insertion point.

---

## 2. Removing Elements

### `remove(value)`
**Purpose:** Remove first occurrence of value

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

```python
numbers = [1, 2, 3, 2]
numbers.remove(2)  # [1, 3, 2] - removes first 2 only
```

**Why O(n)?** Must search for element (O(n)) + shift elements (O(n)) = O(n)

---

### `pop(index=-1)`
**Purpose:** Remove and return element at index (default: last)

**Time Complexity:**
- O(1) for `pop()` or `pop(-1)` (removing from end)
- O(n) for `pop(0)` (removing from beginning)
- O(n-k) for `pop(k)` (removing from middle)

**Space Complexity:** O(1)

```python
numbers = [1, 2, 3, 4, 5]
numbers.pop()      # Returns 5, list: [1, 2, 3, 4] - O(1)
numbers.pop(0)     # Returns 1, list: [2, 3, 4] - O(n)
numbers.pop(1)     # Returns 3, list: [2, 4] - O(n)
```

---

### `clear()`
**Purpose:** Remove all elements

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

```python
numbers = [1, 2, 3, 4, 5]
numbers.clear()  # []
```

---

## 3. Searching & Accessing

### `list[index]`
**Purpose:** Access element at index

**Time Complexity:** O(1)  
**Space Complexity:** O(1)

```python
numbers = [10, 20, 30, 40]
value = numbers[2]  # 30 - direct memory access
```

---

### `index(value, start=0, end=len)`
**Purpose:** Find index of first occurrence

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

```python
numbers = [10, 20, 30, 20]
idx = numbers.index(20)  # 1 (first occurrence)
idx = numbers.index(20, 2)  # 3 (searching from index 2)
```

Raises `ValueError` if not found.

---

### `count(value)`
**Purpose:** Count occurrences of value

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

```python
numbers = [1, 2, 2, 3, 2, 4]
count = numbers.count(2)  # 3
```

---

### `value in list` (membership test)
**Purpose:** Check if value exists

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

```python
numbers = [1, 2, 3, 4, 5]
exists = 3 in numbers  # True - linear search
```

---

## 4. Sorting & Reversing

### `sort(key=None, reverse=False)`
**Purpose:** Sort list in-place

**Time Complexity:** O(n log n)  
**Space Complexity:** O(n) auxiliary space for Timsort

```python
numbers = [3, 1, 4, 1, 5]
numbers.sort()  # [1, 1, 3, 4, 5]

# With key function
words = ['apple', 'pie', 'a', 'cherry']
words.sort(key=len)  # ['a', 'pie', 'apple', 'cherry']
```

Uses **Timsort** algorithm (hybrid of merge sort and insertion sort).

---

### `sorted(list)` (built-in function, not method)
**Purpose:** Return new sorted list

**Time Complexity:** O(n log n)  
**Space Complexity:** O(n)

```python
numbers = [3, 1, 4, 1, 5]
sorted_nums = sorted(numbers)  # [1, 1, 3, 4, 5]
# Original unchanged: [3, 1, 4, 1, 5]
```

---

### `reverse()`
**Purpose:** Reverse list in-place

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

```python
numbers = [1, 2, 3, 4, 5]
numbers.reverse()  # [5, 4, 3, 2, 1]
```

---

### `reversed(list)` (built-in function)
**Purpose:** Return reverse iterator

**Time Complexity:** O(1) to create iterator, O(n) to consume  
**Space Complexity:** O(1)

```python
numbers = [1, 2, 3, 4, 5]
rev = list(reversed(numbers))  # [5, 4, 3, 2, 1]
```

---

## 5. Copying

### `copy()`
**Purpose:** Create shallow copy

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```python
original = [1, 2, 3]
copied = original.copy()  # [1, 2, 3]
```

Equivalent to `list[:]` or `list(original)`.

---

## 6. Other Operations

### `len(list)` (built-in function)
**Purpose:** Get number of elements

**Time Complexity:** O(1)  
**Space Complexity:** O(1)

```python
numbers = [1, 2, 3, 4, 5]
length = len(numbers)  # 5
```

Python stores length as metadata, so it's instant.

---

### `list[start:end:step]` (slicing)
**Purpose:** Extract subsequence

**Time Complexity:** O(k) where k = length of slice  
**Space Complexity:** O(k)

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
subset = numbers[2:7]      # [2, 3, 4, 5, 6] - O(5)
every_second = numbers[::2] # [0, 2, 4, 6, 8] - O(5)
reversed_slice = numbers[::-1]  # O(n)
```

---

## Complete Complexity Table

| Method | Time Complexity | Space Complexity | Notes |
|--------|----------------|------------------|-------|
| `append(x)` | O(1) amortized | O(1) | Fast - preferred for adding |
| `extend(iter)` | O(k) | O(k) | k = length of iterable |
| `insert(i, x)` | O(n) | O(1) | Slow - must shift elements |
| `remove(x)` | O(n) | O(1) | Must search + shift |
| `pop()` | O(1) | O(1) | From end only |
| `pop(0)` | O(n) | O(1) | From beginning - slow |
| `pop(i)` | O(n) | O(1) | From middle - slow |
| `clear()` | O(n) | O(1) | |
| `index(x)` | O(n) | O(1) | Linear search |
| `count(x)` | O(n) | O(1) | Full traversal |
| `x in list` | O(n) | O(1) | Linear search |
| `sort()` | O(n log n) | O(n) | Timsort algorithm |
| `reverse()` | O(n) | O(1) | In-place |
| `copy()` | O(n) | O(n) | Shallow copy |
| `list[i]` | O(1) | O(1) | Direct access |
| `list[i:j]` | O(k) | O(k) | k = j - i |
| `len(list)` | O(1) | O(1) | Stored as metadata |

---

## Performance Comparison Examples

### Adding 10,000 elements

```python
import time

# Fast: append to end
data = []
start = time.time()
for i in range(10000):
    data.append(i)  # O(1) each → O(n) total
print(f"append: {time.time() - start:.4f}s")

# Slow: insert at beginning
data = []
start = time.time()
for i in range(10000):
    data.insert(0, i)  # O(n) each → O(n²) total
print(f"insert(0): {time.time() - start:.4f}s")
```

**Result:** `append()` is ~1000x faster!

---

### Searching

```python
# List - O(n) search
big_list = list(range(1000000))
999999 in big_list  # Checks all 1M elements

# Set - O(1) average search
big_set = set(range(1000000))
999999 in big_set  # Instant lookup
```

---

## Best Practices by Use Case

### Building a List
```python
# Good: O(n)
result = []
for i in range(1000):
    result.append(i)

# Bad: O(n²)
result = []
for i in range(1000):
    result.insert(0, i)
```

### Removing Elements
```python
# Good: O(n) - remove from end
while my_list:
    my_list.pop()

# Bad: O(n²) - remove from beginning
while my_list:
    my_list.pop(0)

# Better for removing from beginning: use collections.deque
from collections import deque
queue = deque([1, 2, 3])
queue.popleft()  # O(1)
```

### Frequent Lookups
```python
# Bad: O(n) for each lookup
if item in my_list:  # Linear search
    ...

# Good: O(1) average for each lookup
my_set = set(my_list)
if item in my_set:  # Hash table lookup
    ...
```

### Sorting
```python
# In-place if you don't need original
numbers.sort()  # O(n log n) time, O(n) space

# New list if you need original
sorted_numbers = sorted(numbers)  # O(n log n) time, O(n) space
```

---

## Memory Considerations

**List Over-allocation:**
Python lists allocate extra space to avoid frequent resizing:

```python
import sys

lst = []
for i in range(10):
    print(f"Length: {len(lst)}, Size: {sys.getsizeof(lst)} bytes")
    lst.append(i)
```

Lists grow by approximately 12.5% each time they need to resize.

---

## When NOT to Use Lists

| Use Case | Don't Use | Use Instead | Why |
|----------|-----------|-------------|-----|
| Frequent insertions at beginning | `list.insert(0, x)` | `collections.deque` | O(1) vs O(n) |
| Frequent membership tests | `x in list` | `set` | O(1) vs O(n) |
| Only need stack operations | `list` | `collections.deque` | More explicit |
| Need sorted order maintained | `list + bisect` | `sortedcontainers.SortedList` | Cleaner API |
| Fixed size, numeric data | `list` | `array.array` or `numpy` | Less memory |

---

**Key Takeaway:** Lists are excellent for sequential access and appending, but consider alternatives for frequent insertions/deletions at beginning or frequent membership tests.

## FAQs

### 1. What is the result of executing: x = [[]] * 3; x[0].append(5); print(x)?
- [[5], [5], [5]]: The multiplication operator * copies the reference to the inner list, so modifying one effectively modifies all of them as they point to the same memory address.

### 2. Which of the following slice operations effectively creates a shallow copy of a list named arr?
- **arr[:]** Using the colon without start or stop indices selects all elements and returns them in a new list object.

### 3. What is the output of a = [1, 2, 3]; b = a; b += [4]; print(a)
- **[1, 2, 3, 4]** For mutable objects like lists, the += operator calls the __iadd__ method, which modifies the original list in-place, affecting all references.

### 4. What happens if you execute t = (1, 2, 3); t += (4,); print(t)?
- A new tuple object is created and assigned to the variable 't'. Because tuples are immutable, the += operator creates a entirely new tuple by concatenating the old one with the new elements.

### 5. How would you sort a list of strings words = ['apple', 'Banana', 'cherry'] alphabetically, ignoring case?
- words.sort(key=str.lower): The key argument applies the function to each element before comparing them, effectively making the sort case-insensitive.

### 6. Which of these methods is the most memory-efficient way to iterate over a very large tuple in reverse?
- reversed(my_tuple) This returns an iterator that yields elements from the end without creating a new copy of the sequence in memory.

