# Python Lists, Sets, and Tuples: Complete Guide with Complexity Analysis

## Overview
This guide covers Python's three fundamental sequence and collection types: lists (mutable sequences), tuples (immutable sequences), and sets (mutable collections of unique elements). Understanding their characteristics and performance is essential for efficient Python programming.

---

# LISTS (Mutable Sequences)

## Core Characteristics
- **Mutable**: Can be modified after creation
- **Ordered**: Maintains insertion order
- **Indexed**: Access elements by position (0-based)
- **Allows Duplicates**: Same value can appear multiple times
- **Dynamic Arrays**: Implemented as resizable arrays

## List Methods and Operations

### 1. Creation and Initialization

#### Basic Creation
```python
# Empty list
my_list = []
my_list = list()

# With initial values
my_list = [1, 2, 3, 4, 5]
my_list = list(range(5))  # [0, 1, 2, 3, 4]
```

#### List Comprehensions
```python
# Basic comprehension
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(20) if x % 2 == 0]

# Nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
```
- **Time Complexity**: O(n) where n is the result size
- **Space Complexity**: O(n)
- **Use Case**: Efficient list creation with transformations

### 2. Access and Indexing

#### Direct Access
```python
my_list = [10, 20, 30, 40, 50]
first = my_list[0]      # 10
last = my_list[-1]      # 50
middle = my_list[2]     # 30
```
- **Time Complexity**: O(1)
- **Space Complexity**: O(1)
- **Use Case**: Fast random access by index

#### Slicing
```python
sub_list = my_list[1:4]    # [20, 30, 40]
reversed_list = my_list[::-1]  # [50, 40, 30, 20, 10]
every_second = my_list[::2]    # [10, 30, 50]
```
- **Time Complexity**: O(k) where k is slice length
- **Space Complexity**: O(k)
- **Use Case**: Extract subsequences efficiently

### 3. Modification Methods

#### `list.append(item)` - Add Single Item
```python
my_list.append(60)  # [10, 20, 30, 40, 50, 60]
```
- **Time Complexity**: O(1) amortized
- **Space Complexity**: O(1)
- **Use Case**: Building lists incrementally
- **Most Efficient**: For adding single items

#### `list.extend(iterable)` - Add Multiple Items
```python
my_list.extend([70, 80])     # Adds each element
my_list.extend("abc")        # Adds 'a', 'b', 'c'
```
- **Time Complexity**: O(k) where k is length of iterable
- **Space Complexity**: O(k)
- **Use Case**: Merging lists or adding multiple elements
- **Faster than**: Multiple append() calls

#### `list.insert(index, item)` - Insert at Position
```python
my_list.insert(0, 5)    # Insert at beginning
my_list.insert(2, 15)   # Insert at index 2
```
- **Time Complexity**: O(n) - must shift elements
- **Space Complexity**: O(1)
- **Use Case**: Insert at specific position
- **Expensive**: For large lists, especially at beginning

#### `list[index] = value` - Assignment
```python
my_list[0] = 100    # Replace first element
my_list[-1] = 200   # Replace last element
```
- **Time Complexity**: O(1)
- **Space Complexity**: O(1)
- **Use Case**: Update existing elements

#### `list[start:end] = iterable` - Slice Assignment
```python
my_list[1:3] = [25, 35, 45]  # Replace slice with new values
my_list[2:2] = [22, 23]      # Insert without replacing
```
- **Time Complexity**: O(n + k) where k is new slice length
- **Space Complexity**: O(k)
- **Use Case**: Replace or insert multiple elements

### 4. Removal Methods

#### `list.remove(value)` - Remove First Occurrence
```python
my_list.remove(30)  # Removes first occurrence of 30
```
- **Time Complexity**: O(n) - must search then shift
- **Space Complexity**: O(1)
- **Use Case**: Remove specific value (first occurrence only)
- **Raises**: ValueError if value not found

#### `list.pop(index=-1)` - Remove and Return
```python
last_item = my_list.pop()     # Remove and return last
first_item = my_list.pop(0)   # Remove and return first
```
- **Time Complexity**: O(1) for last, O(n) for others
- **Space Complexity**: O(1)
- **Use Case**: Stack operations (LIFO) or specific index removal

#### `del list[index]` - Delete by Index
```python
del my_list[2]      # Delete index 2
del my_list[1:3]    # Delete slice
```
- **Time Complexity**: O(1) for last, O(n) for others
- **Space Complexity**: O(1)
- **Use Case**: Simple deletion by index

#### `list.clear()` - Remove All Elements
```python
my_list.clear()  # Empty the list
```
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Use Case**: Reset list while keeping same object

### 5. Search and Query Methods

#### `list.index(value, start=0, stop=len)` - Find Index
```python
index = my_list.index(30)        # Find index of value 30
index = my_list.index(30, 2, 5)  # Search in slice
```
- **Time Complexity**: O(n) - linear search
- **Space Complexity**: O(1)
- **Use Case**: Find position of known value
- **Raises**: ValueError if not found

#### `list.count(value)` - Count Occurrences
```python
count = my_list.count(30)  # How many times 30 appears
```
- **Time Complexity**: O(n) - must scan entire list
- **Space Complexity**: O(1)
- **Use Case**: Frequency counting for specific value

#### `value in list` - Membership Test
```python
exists = 30 in my_list  # Boolean result
```
- **Time Complexity**: O(n) - linear search
- **Space Complexity**: O(1)
- **Use Case**: Check existence before operations

### 6. Ordering Methods

#### `list.sort(key=None, reverse=False)` - In-place Sort
```python
my_list.sort()                    # Ascending order
my_list.sort(reverse=True)        # Descending order
my_list.sort(key=len)             # Sort by custom function
my_list.sort(key=lambda x: -x)    # Sort by negative value
```
- **Time Complexity**: O(n log n) - Timsort algorithm
- **Space Complexity**: O(n) - temporary storage
- **Use Case**: Permanent ordering of list
- **Modifies**: Original list

#### `sorted(list, key=None, reverse=False)` - Return New Sorted List
```python
new_list = sorted(my_list)        # Original unchanged
new_list = sorted(my_list, reverse=True)
```
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n) - creates new list
- **Use Case**: Need sorted version without modifying original

#### `list.reverse()` - Reverse In-place
```python
my_list.reverse()  # Reverses the list
```
- **Time Complexity**: O(n)
- **Space Complexity**: O(1) - in-place operation
- **Use Case**: Reverse order permanently

#### `reversed(list)` - Return Reverse Iterator
```python
for item in reversed(my_list):
    print(item)
```
- **Time Complexity**: O(1) - creates iterator
- **Space Complexity**: O(1)
- **Use Case**: Iterate in reverse without modifying original

### 7. Utility Methods

#### `list.copy()` - Shallow Copy
```python
new_list = my_list.copy()
# Equivalent to: new_list = my_list[:]
```
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Use Case**: Independent copy for modifications
- **Shallow**: Nested objects still referenced

#### `len(list)` - Get Length
```python
size = len(my_list)
```
- **Time Complexity**: O(1) - stored as attribute
- **Space Complexity**: O(1)
- **Use Case**: Size checking, loop bounds

### List Performance Summary

| Operation | Average | Worst Case | Space | Notes |
|-----------|---------|------------|-------|--------|
| Access `list[i]` | O(1) | O(1) | O(1) | Random access |
| Assignment `list[i] = x` | O(1) | O(1) | O(1) | Update element |
| `append()` | O(1) | O(n) | O(1) | Amortized constant |
| `insert(0, x)` | O(n) | O(n) | O(1) | Shift all elements |
| `insert(i, x)` | O(n) | O(n) | O(1) | Shift elements |
| `pop()` | O(1) | O(1) | O(1) | Remove last |
| `pop(0)` | O(n) | O(n) | O(1) | Shift all elements |
| `remove(x)` | O(n) | O(n) | O(1) | Search then shift |
| `index(x)` | O(n) | O(n) | O(1) | Linear search |
| `x in list` | O(n) | O(n) | O(1) | Linear search |
| `sort()` | O(n log n) | O(n log n) | O(n) | Timsort |
| `reverse()` | O(n) | O(n) | O(1) | In-place |

---

# SETS (Mutable Collections of Unique Elements)

## Core Characteristics
- **Mutable**: Can be modified after creation
- **Unordered**: No guaranteed order (Python 3.7+ maintains insertion order)
- **Unique Elements**: Automatically removes duplicates
- **Hash Table**: Fast membership testing
- **Hashable Elements Only**: Elements must be immutable

## Set Methods and Operations

### 1. Creation and Initialization

#### Basic Creation
```python
# Empty set
my_set = set()          # Note: {} creates empty dict, not set
my_set = {1, 2, 3, 4}   # Set literal

# From iterable
my_set = set([1, 2, 2, 3, 3, 4])  # {1, 2, 3, 4} - duplicates removed
my_set = set("hello")              # {'h', 'e', 'l', 'o'} - duplicates removed
```

#### Set Comprehensions
```python
squares = {x**2 for x in range(10)}
evens = {x for x in range(20) if x % 2 == 0}
```
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Use Case**: Create sets with transformations

### 2. Modification Methods

#### `set.add(element)` - Add Single Element
```python
my_set.add(5)    # Adds 5 to set
my_set.add(3)    # No effect if 3 already exists
```
- **Time Complexity**: O(1) average, O(n) worst case
- **Space Complexity**: O(1)
- **Use Case**: Add single element
- **Idempotent**: No change if element exists

#### `set.update(iterable)` - Add Multiple Elements
```python
my_set.update([6, 7, 8])
my_set.update("abc")        # Adds 'a', 'b', 'c'
my_set.update({9, 10})      # From another set
```
- **Time Complexity**: O(k) where k is length of iterable
- **Space Complexity**: O(k) for new elements
- **Use Case**: Bulk addition from any iterable

#### `set.remove(element)` - Remove Element (with Exception)
```python
my_set.remove(5)  # Removes 5 from set
# Raises KeyError if element doesn't exist
```
- **Time Complexity**: O(1) average, O(n) worst case
- **Space Complexity**: O(1)
- **Use Case**: Remove known element
- **Strict**: Raises exception if not found

#### `set.discard(element)` - Remove Element (Safe)
```python
my_set.discard(5)   # Removes 5 if present
my_set.discard(99)  # No error if 99 not present
```
- **Time Complexity**: O(1) average, O(n) worst case
- **Space Complexity**: O(1)
- **Use Case**: Safe removal without exceptions
- **Preferred**: For uncertain element existence

#### `set.pop()` - Remove and Return Arbitrary Element
```python
element = my_set.pop()  # Removes and returns arbitrary element
```
- **Time Complexity**: O(1)
- **Space Complexity**: O(1)
- **Use Case**: Get and remove any element
- **Raises**: KeyError if set is empty
- **Arbitrary**: No guarantee which element is returned

#### `set.clear()` - Remove All Elements
```python
my_set.clear()  # Empties the set
```
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Use Case**: Reset set

### 3. Query Methods

#### `element in set` - Membership Test
```python
exists = 5 in my_set  # Fast membership testing
```
- **Time Complexity**: O(1) average, O(n) worst case
- **Space Complexity**: O(1)
- **Use Case**: Fast existence checking
- **Main Advantage**: Much faster than list membership

#### `len(set)` - Get Size
```python
size = len(my_set)
```
- **Time Complexity**: O(1)
- **Space Complexity**: O(1)
- **Use Case**: Size checking

### 4. Set Operations (Mathematical)

#### Union: `set1 | set2` or `set1.union(set2)`
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2          # {1, 2, 3, 4, 5}
union_set = set1.union(set2)     # Same result
```
- **Time Complexity**: O(len(set1) + len(set2))
- **Space Complexity**: O(len(set1) + len(set2))
- **Use Case**: Combine elements from multiple sets
- **Mathematical**: A ∪ B

#### Intersection: `set1 & set2` or `set1.intersection(set2)`
```python
intersection_set = set1 & set2              # {3}
intersection_set = set1.intersection(set2)  # Same result
```
- **Time Complexity**: O(min(len(set1), len(set2)))
- **Space Complexity**: O(min(len(set1), len(set2)))
- **Use Case**: Find common elements
- **Mathematical**: A ∩ B

#### Difference: `set1 - set2` or `set1.difference(set2)`
```python
difference_set = set1 - set2              # {1, 2}
difference_set = set1.difference(set2)    # Same result
```
- **Time Complexity**: O(len(set1))
- **Space Complexity**: O(len(set1))
- **Use Case**: Elements in first set but not second
- **Mathematical**: A - B

#### Symmetric Difference: `set1 ^ set2` or `set1.symmetric_difference(set2)`
```python
sym_diff_set = set1 ^ set2                        # {1, 2, 4, 5}
sym_diff_set = set1.symmetric_difference(set2)    # Same result
```
- **Time Complexity**: O(len(set1) + len(set2))
- **Space Complexity**: O(len(set1) + len(set2))
- **Use Case**: Elements in either set but not both
- **Mathematical**: (A ∪ B) - (A ∩ B)

### 5. In-place Set Operations

#### `set1.update()` - Union In-place
```python
set1.update(set2)  # set1 = set1 | set2
```

#### `set1.intersection_update()` - Intersection In-place
```python
set1.intersection_update(set2)  # set1 = set1 & set2
```

#### `set1.difference_update()` - Difference In-place
```python
set1.difference_update(set2)  # set1 = set1 - set2
```

#### `set1.symmetric_difference_update()` - Symmetric Difference In-place
```python
set1.symmetric_difference_update(set2)  # set1 = set1 ^ set2
```

### 6. Set Relationship Tests

#### `set1.issubset(set2)` - Subset Test
```python
is_subset = set1.issubset(set2)  # set1 <= set2
```
- **Time Complexity**: O(len(set1))
- **Use Case**: Check if all elements of set1 are in set2

#### `set1.issuperset(set2)` - Superset Test
```python
is_superset = set1.issuperset(set2)  # set1 >= set2
```
- **Time Complexity**: O(len(set2))
- **Use Case**: Check if set1 contains all elements of set2

#### `set1.isdisjoint(set2)` - Disjoint Test
```python
is_disjoint = set1.isdisjoint(set2)  # No common elements
```
- **Time Complexity**: O(min(len(set1), len(set2)))
- **Use Case**: Check if sets have no common elements

### 7. Set Utility Methods

#### `set.copy()` - Shallow Copy
```python
new_set = my_set.copy()
```
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Use Case**: Independent copy

### Set Performance Summary

| Operation | Average | Worst Case | Space | Notes |
|-----------|---------|------------|-------|--------|
| `add(x)` | O(1) | O(n) | O(1) | Hash table insert |
| `remove(x)` | O(1) | O(n) | O(1) | Hash table delete |
| `x in set` | O(1) | O(n) | O(1) | Hash table lookup |
| `union()` | O(m+n) | O(m+n) | O(m+n) | Create new set |
| `intersection()` | O(min(m,n)) | O(min(m,n)) | O(min(m,n)) | Smaller set size |
| `difference()` | O(m) | O(m) | O(m) | First set size |
| `update()` | O(k) | O(k) | O(k) | k = elements added |

---

# TUPLES (Immutable Sequences)

## Core Characteristics
- **Immutable**: Cannot be modified after creation
- **Ordered**: Maintains order of elements
- **Indexed**: Access elements by position (0-based)
- **Allows Duplicates**: Same value can appear multiple times
- **Hashable**: Can be used as dictionary keys or set elements
- **Memory Efficient**: More compact than lists

## Tuple Operations

### 1. Creation and Initialization

#### Basic Creation
```python
# Empty tuple
empty_tuple = ()
empty_tuple = tuple()

# Single element (comma required)
single_tuple = (42,)  # Note the comma
single_tuple = 42,    # Parentheses optional

# Multiple elements
my_tuple = (1, 2, 3, 4, 5)
my_tuple = 1, 2, 3, 4, 5  # Parentheses optional

# From iterable
my_tuple = tuple([1, 2, 3, 4])
my_tuple = tuple("hello")  # ('h', 'e', 'l', 'l', 'o')
```

#### Tuple Comprehensions (Generator Expressions)
```python
# Actually creates a generator, convert to tuple if needed
gen = (x**2 for x in range(10))
squares_tuple = tuple(gen)
```

### 2. Access and Indexing (Same as Lists)

#### Direct Access
```python
my_tuple = (10, 20, 30, 40, 50)
first = my_tuple[0]      # 10
last = my_tuple[-1]      # 50
```
- **Time Complexity**: O(1)
- **Space Complexity**: O(1)

#### Slicing
```python
sub_tuple = my_tuple[1:4]    # (20, 30, 40)
reversed_tuple = my_tuple[::-1]  # (50, 40, 30, 20, 10)
```
- **Time Complexity**: O(k) where k is slice length
- **Space Complexity**: O(k)

### 3. Query Methods

#### `tuple.index(value, start=0, stop=len)` - Find Index
```python
index = my_tuple.index(30)  # Find index of value 30
```
- **Time Complexity**: O(n) - linear search
- **Space Complexity**: O(1)
- **Raises**: ValueError if not found

#### `tuple.count(value)` - Count Occurrences
```python
count = my_tuple.count(30)  # How many times 30 appears
```
- **Time Complexity**: O(n) - must scan entire tuple
- **Space Complexity**: O(1)

#### `value in tuple` - Membership Test
```python
exists = 30 in my_tuple  # Boolean result
```
- **Time Complexity**: O(n) - linear search
- **Space Complexity**: O(1)

#### `len(tuple)` - Get Length
```python
size = len(my_tuple)
```
- **Time Complexity**: O(1)
- **Space Complexity**: O(1)

### 4. Tuple Unpacking and Packing

#### Basic Unpacking
```python
point = (3, 4)
x, y = point  # x=3, y=4

# With underscore for unused values
data = (1, 2, 3, 4, 5)
first, second, *rest = data  # first=1, second=2, rest=[3,4,5]
first, *middle, last = data  # first=1, middle=[2,3,4], last=5
```
- **Time Complexity**: O(n) for unpacking n elements
- **Use Case**: Multiple assignment, function returns

#### Swapping Variables
```python
a, b = b, a  # Elegant variable swapping
```
- **Time Complexity**: O(1)
- **Use Case**: Variable swapping without temporary variables

#### Function Arguments
```python
def func(a, b, c):
    return a + b + c

args = (1, 2, 3)
result = func(*args)  # Unpacking tuple as arguments
```

### 5. Named Tuples

#### Using `collections.namedtuple`
```python
from collections import namedtuple

# Create named tuple class
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', 'name age city')

# Create instances
p1 = Point(3, 4)
person = Person('Alice', 30, 'New York')

# Access by name or index
print(p1.x, p1.y)        # 3 4
print(p1[0], p1[1])      # 3 4
print(person.name)        # Alice
```
- **Immutable**: Like regular tuples
- **Named Access**: More readable than index access
- **Memory Efficient**: Less overhead than classes
- **Use Case**: Simple data structures, configuration

### 6. Tuple Utility Operations

#### Concatenation
```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2  # (1, 2, 3, 4, 5, 6)
```
- **Time Complexity**: O(n + m)
- **Space Complexity**: O(n + m)
- **Creates**: New tuple (original unchanged)

#### Repetition
```python
repeated = (1, 2) * 3  # (1, 2, 1, 2, 1, 2)
```
- **Time Complexity**: O(n * k) where k is repetition count
- **Space Complexity**: O(n * k)

#### Comparison
```python
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
print(tuple1 < tuple2)  # True - lexicographic comparison
```
- **Time Complexity**: O(min(n, m))
- **Space Complexity**: O(1)
- **Lexicographic**: Element-wise comparison

### Tuple Performance Summary

| Operation | Time | Space | Notes |
|-----------|------|-------|--------|
| Access `tuple[i]` | O(1) | O(1) | Random access |
| `index(x)` | O(n) | O(1) | Linear search |
| `count(x)` | O(n) | O(1) | Full scan |
| `x in tuple` | O(n) | O(1) | Linear search |
| `len(tuple)` | O(1) | O(1) | Stored attribute |
| Slice `tuple[i:j]` | O(j-i) | O(j-i) | New tuple |
| Concatenation `+` | O(n+m) | O(n+m) | New tuple |
| Repetition `*` | O(n*k) | O(n*k) | New tuple |

---

# COMPARISON AND WHEN TO USE EACH

## Performance Characteristics Comparison

### Memory Usage
```python
import sys

# Memory comparison (approximate)
list_mem = sys.getsizeof([1, 2, 3, 4, 5])    # ~104 bytes
tuple_mem = sys.getsizeof((1, 2, 3, 4, 5))   # ~80 bytes
set_mem = sys.getsizeof({1, 2, 3, 4, 5})     # ~224 bytes

# Tuples are most memory efficient for sequences
# Sets have overhead for hash table structure
```

### Speed Comparison for Common Operations

| Operation | List | Tuple | Set | Winner |
|-----------|------|-------|-----|---------|
| Creation | O(n) | O(n) | O(n) | Tuple (fastest) |
| Access by index | O(1) | O(1) | N/A | Tie |
| Membership test | O(n) | O(n) | O(1) | **Set** |
| Append/Add | O(1) | N/A | O(1) | Tie |
| Insert at beginning | O(n) | N/A | O(1) | Set |
| Remove element | O(n) | N/A | O(1) | Set |
| Sort | O(n log n) | N/A | N/A | List only |

## Use Case Guidelines

### Use Lists When:
- Need mutable, ordered collection
- Require indexing and slicing
- Need to maintain duplicates
- Frequent appending to end
- Need sorting capability
- Building collections incrementally

```python
# Examples
shopping_cart = []
shopping_cart.append("milk")
shopping_cart.append("bread")

grades = [85, 92, 78, 85, 90]  # Duplicates allowed
grades.sort()

game_moves = ["up", "right", "down", "left"]
last_move = game_moves[-1]
```

### Use Tuples When:
- Need immutable, ordered collection
- Want to ensure data doesn't change
- Need hashable sequence (for dict keys/set elements)
- Representing fixed structures (coordinates, RGB colors)
- Function returns multiple values
- Memory efficiency is important
- Configuration or constant data

```python
# Examples
RGB_RED = (255, 0, 0)  # Color constant
point = (10, 20)       # Coordinate
dimensions = (1920, 1080, 24)  # Width, height, depth

# Multiple return values
def get_name_age():
    return "Alice", 30

name, age = get_name_age()

# Dictionary keys
locations = {
    (0, 0): "origin",
    (10, 20): "point_a",
    (30, 40): "point_b"
}
```

### Use Sets When:
- Need unique elements only
- Frequent membership testing
- Mathematical set operations
- Removing duplicates from sequences
- Fast add/remove operations
- Don't need ordering or indexing

```python
# Examples
# Remove duplicates
unique_items = set([1, 2, 2, 3, 3, 4])  # {1, 2, 3, 4}

# Fast membership testing
valid_ids = {100, 101, 102, 103, 104}
if user_id in valid_ids:  # O(1) lookup
    grant_access()

# Set operations
python_users = {"Alice", "Bob", "Charlie"}
java_users = {"Bob", "David", "Eve"}
both_languages = python_users & java_users  # {"Bob"}
all_users = python_users | java_users

# Tracking seen items
seen = set()
for item in data:
    if item not in seen:
        process(item)
        seen.add(item)
```

## Best Practices and Patterns

### 1. Converting Between Types
```python
# List to set (remove duplicates)
unique_list = list(set(original_list))

# Set to sorted list
sorted_unique = sorted(my_set)

# Tuple to list (for modification)
mutable_copy = list(my_tuple)
```

### 2. Memory-Efficient Patterns
```python
# Use tuple for read-only data
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

# Use set for membership tests
VALID_EXTENSIONS = {".jpg", ".png", ".gif", ".svg"}

if file_extension in VALID_EXTENSIONS:
    process_image()
```

### 3. Algorithm Selection
```python
# For frequent lookups: use set
def has_duplicates_efficient(items):
    seen = set()
    for item in items:
        if item in seen:  # O(1) lookup
            return True
        seen.add(item)
    return False

# For ordered operations: use list
def merge_sorted_lists(list1, list2):
    result = []
    i = j = 0
    # ... merge logic using indexing
    return result

# For immutable return values: use tuple
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)
```
