from collections import defaultdict
"""
Reverse a Dictionary:

    Convert {a: 1, b: 2} → {1: a, 2: b}
    What if values are not unique?
    ---------------------------------------------
"""
hm = {'a': 1, 'b': 2, 'c':2, 'd':0, 'e':'x'}
reversed_hm = {val:key for key, val in hm.items()}
print(reversed_hm)

# What if values are duplicates: Store Multiple Keys in a List
# “If dictionary values are not unique, reversing directly causes key collisions.
# To preserve all data, I store the original keys in a list.”
reversed_hm = {}

for key, val in hm.items():

    if val not in reversed_hm:
        reversed_hm[val] = []
    reversed_hm[val].append(key)
print(reversed_hm)

# Using default dict
reversed_hm = defaultdict(list)
for key, val in hm.items():
    reversed_hm[val].append(key)
print(reversed_hm)

# Invalid reversal:
d = {'a': [1, 2], 'b': [3, 4]} # List as key not hashable
# “Reversing a dictionary assumes that all values are hashable.
# If values are mutable types like lists or dicts, they cannot become keys and the reverse operation fails.”
def safe_reverse_dict(d):
    result = {}

    for k, v in d.items():
        if not isinstance(v, (int, str, tuple, frozenset)):
            raise TypeError(f"Unhashable value: {v}")
        result[v] = k

    return result

print(safe_reverse_dict(d))


