# Core Memory Architecture in Python
In Python, everything is an object stored on the heap. Even a simple integer isn't just 5 in memory—it's a full-fledged object:

```Python
import sys

x = 5
print(sys.getsizeof(x))  # 28 bytes (not just 4!)
```

**Why so large?** Each object contains:
- **Reference count** (8 bytes) - tracks how many variables point to it
- **Type pointer** (8 bytes) - points to the object's type
- **Actual value** (4 bytes for int) - the data itself
- **Padding/overhead** (~8 bytes) - memory alignment

**Analogy**: Think of objects like registered packages at a post office. You don't just have the item—you have tracking info, metadata, and a storage bin number.

## **Memory Management in Python**

### 1. Memory Allocation
Python uses a private heap to store all objects and data structures. You never access this heap directly — the Python memory manager handles it internally.

There are two layers:

1. **System allocator** — Python requests large memory blocks from the OS.
2. **PyMalloc** — Python's internal allocator, optimized for small objects (≤ 512 bytes). It carves up those large blocks into smaller chunks efficiently.

Python maintains its own **private heap** separate from the system heap:
```
┌─────────────────────────────────────┐
│     Python's Private Heap           │
│  ┌──────────────────────────────┐   │
│  │   Arena (256 KB chunks)      │   │
│  │  ┌────────┬────────┬──────┐  │   │
│  │  │ Pool 1 │ Pool 2 │ ...  │  │   │
│  │  └────────┴────────┴──────┘  │   │
│  └──────────────────────────────┘   │
└─────────────────────────────────────┘
Memory tiers:

Small objects (<512 bytes): Managed by Python's object allocator (fast pools)
Large objects (>512 bytes): Directly use system malloc/free (slower)
```
### 2. Reference Counting
Every Python object has a reference count — a number tracking how many **variables/structures** point to it.

```python
a = [1, 2, 3]   # ref count = 1
b = a            # ref count = 2
del a            # ref count = 1
del b            # ref count = 0 → object is deallocated immediately
```

- When the count hits zero, memory is freed right away. You can inspect it with `sys.getrefcount()`.

- **Limitation**: Reference counting can't handle circular references:
```python
a = {}
b = {}
a['ref'] = b
b['ref'] = a  # both have ref count ≥ 1, even if nothing else points to them
```

### 3. Garbage Collector (GC)
To handle circular references, Python has a **cyclic garbage collector** (gc module). It runs periodically and detects reference cycles that reference counting misses.

It uses a generational collection strategy — objects are grouped into 3 generations:

#### How the Cyclic GC Detects It

```text
Step 1: Find all container objects (dict, list, class instances, etc.)
Step 2: For each object, copy its real ref count into a temporary counter
Step 3: Traverse all references and DECREMENT the temp counter for each
Step 4: Any object with temp counter > 0 is reachable from outside → SAFE
Step 5: Any object with temp counter == 0 is UNREACHABLE → garbage
```

#### Let's visualize it:

```text
Before GC trial deletion:
  obj_a  →  temp_rc = 2  (1 from 'a' var + 1 from b['ref'])
  obj_b  →  temp_rc = 2  (1 from 'b' var + 1 from a['ref'])

After del a, del b:
  obj_a  →  temp_rc = 1  (only b['ref'] points to it)
  obj_b  →  temp_rc = 1  (only a['ref'] points to it)

GC traverses internal references and decrements:
  obj_a  →  temp_rc = 1 - 1 = 0  ← UNREACHABLE 🗑️
  obj_b  →  temp_rc = 1 - 1 = 0  ← UNREACHABLE 🗑️
```

### 4. Object Interning
Python reuses certain immutable objects instead of creating new ones:
- Small integers (-5 to 256) are cached permanently.
- Short strings that look like identifiers are interned.

```python
a = 100
b = 100
print(a is b)   # True  → same object in memory

a = 1000
b = 1000
print(a is b)   # False → different objects
```