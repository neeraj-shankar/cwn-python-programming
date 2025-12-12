# Python Dictionary Methods: Complete Guide with Complexity Analysis

## Overview
Python dictionaries are hash tables that provide efficient key-value storage. Understanding the time and space complexity of various dictionary operations is crucial for writing performant code.

## Core Dictionary Methods

### 1. Access and Retrieval Methods

#### `dict[key]` - Direct Access
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
value = my_dict['a']  # Returns 1
```
- **Use Case**: Fast key lookup when you're certain the key exists
- **Time Complexity**: O(1) average, O(n) worst case
- **Space Complexity**: O(1)
- **Note**: Raises KeyError if key doesn't exist

#### `dict.get(key, default=None)` - Safe Access
```python
value = my_dict.get('d', 'Not Found')  # Returns 'Not Found'
value = my_dict.get('a')  # Returns 1
```
- **Use Case**: Safe key lookup with fallback value
- **Time Complexity**: O(1) average, O(n) worst case
- **Space Complexity**: O(1)
- **Advantage**: No exception thrown for missing keys

#### `dict.setdefault(key, default=None)` - Get or Set
```python
my_dict.setdefault('d', 4)  # Adds 'd': 4 and returns 4
my_dict.setdefault('a', 10)  # Returns existing value 1, doesn't change
```
- **Use Case**: Initialize key with default if it doesn't exist
- **Time Complexity**: O(1) average, O(n) worst case
- **Space Complexity**: O(1)
- **Common Pattern**: Building nested dictionaries or lists

### 2. Modification Methods

#### `dict[key] = value` - Assignment
```python
my_dict['e'] = 5  # Adds new key-value pair
my_dict['a'] = 10  # Updates existing value
```
- **Use Case**: Adding or updating key-value pairs
- **Time Complexity**: O(1) average, O(n) worst case
- **Space Complexity**: O(1) for updates, O(1) amortized for new keys

#### `dict.update(other)` - Bulk Update
```python
my_dict.update({'f': 6, 'g': 7})
my_dict.update([('h', 8), ('i', 9)])
my_dict.update(j=10, k=11)
```
- **Use Case**: Merging dictionaries or bulk updates
- **Time Complexity**: O(m) where m is the number of items being added
- **Space Complexity**: O(m) for new keys
- **Versatile**: Accepts dict, iterable of pairs, or keyword arguments

#### `dict.pop(key, default)` - Remove and Return
```python
value = my_dict.pop('a')  # Removes 'a' and returns its value
value = my_dict.pop('z', 'Not Found')  # Safe removal with default
```
- **Use Case**: Remove key and get its value atomically
- **Time Complexity**: O(1) average, O(n) worst case
- **Space Complexity**: O(1)
- **Advantage**: Atomic remove-and-return operation

#### `dict.popitem()` - Remove Last Item (Python 3.7+)
```python
key, value = my_dict.popitem()  # Removes and returns last inserted item
```
- **Use Case**: LIFO removal, implementing stack-like behavior
- **Time Complexity**: O(1)
- **Space Complexity**: O(1)
- **Note**: Order guaranteed since Python 3.7

#### `del dict[key]` - Delete Key
```python
del my_dict['b']  # Removes key 'b'
```
- **Use Case**: Simple key removal
- **Time Complexity**: O(1) average, O(n) worst case
- **Space Complexity**: O(1)
- **Note**: Raises KeyError if key doesn't exist

#### `dict.clear()` - Remove All Items
```python
my_dict.clear()  # Empties the dictionary
```
- **Use Case**: Reset dictionary while keeping the same object
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### 3. Query Methods

#### `key in dict` - Membership Test
```python
exists = 'a' in my_dict  # Returns Boolean
```
- **Use Case**: Check if key exists before operations
- **Time Complexity**: O(1) average, O(n) worst case
- **Space Complexity**: O(1)
- **Most Efficient**: For existence checking

#### `dict.keys()` - Get All Keys
```python
keys = my_dict.keys()  # Returns dict_keys view
key_list = list(my_dict.keys())  # Convert to list if needed
```
- **Use Case**: Iterate over keys, key-based operations
- **Time Complexity**: O(1) for view creation, O(n) for list conversion
- **Space Complexity**: O(1) for view, O(n) for list
- **Dynamic**: View reflects dictionary changes

#### `dict.values()` - Get All Values
```python
values = my_dict.values()  # Returns dict_values view
```
- **Use Case**: Iterate over values, value-based analysis
- **Time Complexity**: O(1) for view creation
- **Space Complexity**: O(1) for view, O(n) for list conversion
- **Note**: Values may contain duplicates

#### `dict.items()` - Get Key-Value Pairs
```python
items = my_dict.items()  # Returns dict_items view
for key, value in my_dict.items():
    print(f"{key}: {value}")
```
- **Use Case**: Iterate over both keys and values
- **Time Complexity**: O(1) for view creation
- **Space Complexity**: O(1) for view
- **Most Common**: For dictionary iteration

### 4. Advanced Methods

#### `dict.copy()` - Shallow Copy
```python
new_dict = my_dict.copy()
```
- **Use Case**: Create independent copy for modifications
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- **Shallow**: Nested objects are still referenced

#### `dict.fromkeys(iterable, value=None)` - Create from Keys
```python
new_dict = dict.fromkeys(['a', 'b', 'c'], 0)
# Creates {'a': 0, 'b': 0, 'c': 0}
```
- **Use Case**: Initialize multiple keys with same value
- **Time Complexity**: O(n) where n is length of iterable
- **Space Complexity**: O(n)
- **Warning**: Mutable default values are shared references

## Performance Characteristics

### Hash Table Properties
- **Average Case**: O(1) for most operations due to hash table implementation
- **Worst Case**: O(n) when many hash collisions occur
- **Load Factor**: Python resizes when load factor exceeds 2/3
- **Memory Overhead**: ~33% overhead for hash table structure

### Complexity Summary Table

| Operation | Average | Worst Case | Space | Notes |
|-----------|---------|------------|-------|--------|
| Access `dict[key]` | O(1) | O(n) | O(1) | Fastest lookup |
| Assignment `dict[key] = val` | O(1) | O(n) | O(1) | May trigger resize |
| `get()` | O(1) | O(n) | O(1) | Safe access |
| `pop()` | O(1) | O(n) | O(1) | Remove and return |
| `in` operator | O(1) | O(n) | O(1) | Membership test |
| `update()` | O(m) | O(n+m) | O(m) | m = items added |
| `keys()/values()/items()` | O(1) | O(1) | O(1) | View creation |
| `copy()` | O(n) | O(n) | O(n) | Full dictionary copy |
| `clear()` | O(n) | O(n) | O(1) | Remove all items |

## Best Practices and Use Cases

### 1. Choosing the Right Method
```python
# For safe access with default
value = my_dict.get(key, default_value)

# For initialization patterns
my_dict.setdefault(key, []).append(item)

# For existence checking
if key in my_dict:
    # Process existing key

# For iteration
for key, value in my_dict.items():
    # Process each pair
```

### 2. Common Patterns

#### Grouping Items
```python
# Using setdefault
groups = {}
for item in items:
    groups.setdefault(item.category, []).append(item)

# Using defaultdict (alternative)
from collections import defaultdict
groups = defaultdict(list)
for item in items:
    groups[item.category].append(item)
```

#### Safe Dictionary Operations
```python
# Safe removal
value = my_dict.pop(key, None)
if value is not None:
    process(value)

# Safe access with processing
if key in my_dict:
    result = expensive_operation(my_dict[key])
```

#### Merging Dictionaries
```python
# Python 3.9+
merged = dict1 | dict2

# Earlier versions
merged = {**dict1, **dict2}

# In-place update
dict1.update(dict2)
```

## Memory Considerations

### Dictionary Resizing
- Dictionaries resize when load factor exceeds ~0.67
- Resizing creates a new hash table (temporarily doubles memory usage)
- Consider pre-sizing for large known datasets

### Memory-Efficient Alternatives
```python
# For read-only mappings
from types import MappingProxyType
readonly_dict = MappingProxyType(my_dict)

# For memory-efficient counting
from collections import Counter
counts = Counter(items)  # More efficient than manual dict counting
```

## Conclusion

Python dictionaries are highly optimized data structures with excellent average-case performance. Understanding when and how to use different methods can significantly impact your code's performance and readability. The key is choosing the right method for your specific use case while being aware of the complexity trade-offs.