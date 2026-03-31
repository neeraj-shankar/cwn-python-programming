# Comprensive Guide on Understanding and using list.

## List 
- A List is a linear data structure that stores an ordered collection of elements, where elements can be accessed by their index and duplicates are allowed.
- Python lists support methods for insertion, deletion, searching, sorting, and copying, such as append, pop, remove, sort, and copy.
- Most list methods work in-place and return None (like sort(), reverse(), append())
-----

### 1. **`append()`**
- Adds one element to the end of the list. Takes a single object and that object is added **as-is**.

### 2. **`extend()`**
- Adds multiple elements from another iterable to the list. Takes an iterable and adds elements one by one.

#### ***👉 Comparison***
- **append()** adds a single element to the list, while **extend()** adds all elements from another iterable individually.
_____

```python
# Example of the append
a = [1, 2, 3]
b = [5, 6]
a.append(4) # [1, 2, 3, 4]
a.append(b) # [1, 2, 3, 4, [5, 6]]

# Example of the extend operation
a = [1, 2, 3]
b = [5, 6]
a.extend(b) # [1, 2, 3, 5, 6]
a. extend(4) # 

```
_____

### 3. **`remove()`**
- Removes the first occurrence of a given value from the list. Raises **ValueError** if element not found
- It does not return anything.
- **Time Complexity:** O(n) (needs to search)
- **Space Complexity:** O(1)

### 4. **`pop()`:**
- Removes and returns the element at given index (default: last). Raises **IndexError** if index invalid
- **Time Complexity:** **O(1)** → if popping last element where as **O(n)** → if popping from middle/front (shifting)
- **Space Complexity:** O(1)
_____

#### ***👉 Note:*** 
* `remove()` deletes by value and requires searching, while `pop()` deletes by index and also returns the removed element. 
* Both methods modify the list **in-place** and may require shifting elements, which is why middle deletions are *O(n)*.
_____

### 5. **`insert(idx, x)`:**
- Inserts an element **x** at index **idx**, shifting existing elements to the right.
- Takes index and value. Modifies the list in-place and does not return anything.

##### **👉Note:**
- Inserting at the end using `insert(len(list), x)` is still O(1) amortized, but `append()` is preferred for clarity and performance.
-----

### Comparison Table of different list methods
| Method             | Description           | Time Complexity    | Space Complexity |
| ------------------ | --------------------- | ------------------ | ---------------- |
| `append(x)`        | Add element at end    | **O(1)** amortized | O(1)             |
| `extend(iterable)` | Add multiple elements | O(k)               | O(1)             |
| `insert(i, x)`     | Insert at index       | **O(n)**           | O(1)             |
| `remove(x)`        | Remove by value       | **O(n)**           | O(1)             |
| `pop()`            | Remove last element   | **O(1)**           | O(1)             |
| `pop(i)`           | Remove at index       | **O(n)**           | O(1)             |
| `clear()`          | Remove all elements   | O(n)               | O(1)             |
| `index(x)`         | Find index of value   | **O(n)**           | O(1)             |
| `count(x)`         | Count occurrences     | **O(n)**           | O(1)             |
| `sort()`           | Sort list             | **O(n log n)**     | O(1)*            |
| `reverse()`        | Reverse list          | **O(n)**           | O(1)             |
| `copy()`           | Shallow copy          | **O(n)**           | O(n)             |
| `len(list)`        | Get length            | **O(1)**           | O(1)             |
-----

### When NOT to Use Lists

| Use Case | Don't Use | Use Instead | Why |
|----------|-----------|-------------|-----|
| Frequent insertions at beginning | `list.insert(0, x)` | `collections.deque` | O(1) vs O(n) |
| Frequent membership tests | `x in list` | `set` | O(1) vs O(n) |
| Only need stack operations | `list` | `collections.deque` | More explicit |
| Need sorted order maintained | `list + bisect` | `sortedcontainers.SortedList` | Cleaner API |
| Fixed size, numeric data | `list` | `array.array` or `numpy` | Less memory |

-----
-----

## Sets
- A set in Python is a collection data type that stores unique elements in an unordered manner.
- It is implemented using a **hash table**, which allows average **O(1)** time complexity for insertion, deletion, and lookup operations.
- It does not support indexing or slicing
- Set operations like add, remove, and membership checks run in O(1) on average due to hashing, making sets ideal for fast lookup and uniqueness enforcement.

### 1. **`remove()` and `discard()`**
- While both remove elements **x** from a set. However, **remove()** throws an error if the element is missing, while **discard()** fails silently.
- Prefer **discard()** in production code when you're not 100% sure the element exists, to avoid unnecessary exceptions.
- Removes duplicates automatically and does **not modify** original sets

### 2. **`union`:**
- Returns a new set containing all unique elements from both sets.
- Removes duplicates automatically and does not modify original sets.
- Can also use | operator

### 3. **`intersection()`:**
- Returns a new set containing only the elements that are common to both sets.
- Removes duplicates automatically and does not modify original sets
- Can also use & operator

### 4. **`symmetric_difference()`:**
- Returns elements that are in either set, but NOT in both.
- That is, elements that are present in both sets will be excluded.
- symmetric_difference() is equivalent to: **(A - B) ∪ (B - A)**

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union_set = A.union(B) # {1, 2, 3, 4, 5, 6}
intersect_set = A.intersection(B) # {3, 4}

only_in_A = (A-B) # {1, 2}
only_in_B = (B-A) # {5, 6}

sym_diff = only_in_A | only_in_B # {1, 2, 5, 6}
```
#### **👉Note:**
- Time and Complexity of intersection is **O(min(n, m))** because Python iterates over the smaller set and checks membership in the larger one.
- `union()` returns all elements from both sets, while `symmetric_difference()` returns only the elements that are not common to both.
-----

### Summary Table of Set
| Method                          | Description                         | Time Complexity(Avg) | SC
| ------------------------------- | ----------------------------------- | --------------------- | -------------
| `add(x)`                        | Add element to set                  | **O(1)**              | O(1)
| `remove(x)`                     | Remove element (error if not found) | **O(1)**              | O(1)
| `discard(x)`                    | Remove element (no error)           | **O(1)**              | O(1)
| `pop()`                         | Remove & return arbitrary element   | **O(1)**              | O(1)
| `clear()`                       | Remove all elements                 | O(n)                  | O(1)
| `copy()`                        | Shallow copy                        | O(n)                  | O(n)
| `union(s)` / `                  | Combine two sets                    | O(n + m)              | O(n + m) |
| `intersection(s)` / `&`         | Common elements                     | O(min(n, m))          | O(min(n, m))
| `difference(s)` / `-`           | Elements in first not in second     | O(n)                  | O(n)
| `symmetric_difference(s)` / `^` | Elements in either, not both        | O(n + m)              | O(n + m)
| `issubset(s)`                   | Check subset                        | O(n)                  | O(1)
| `issuperset(s)`                 | Check superset                      | O(m)                  | O(1)
| `isdisjoint(s)`                 | No common elements?                 | O(min(n, m))          | O(1)
| `len(set)`                      | Number of elements                  | **O(1)**              | O(1)
| `x in set`                      | Membership test                     | **O(1)**              | O(1)

-----
-----

### FAQs

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

