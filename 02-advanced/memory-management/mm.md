# Core Memory Architecture in Python

## 1. Everything is a PyObject
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

### **2. Memory Pools - Private Heap**

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