"""
Remove all keys with None values.
---------------------------------------
“I iterate through the dictionary and construct a new dictionary excluding keys whose value is None.
Using is not None avoids removing valid falsy values.”
"""

hm = {'a': 1, 'b':1, 'c':None, 'd':None}

# Using comprehension 
cleaned_hm = {key: val for key, val in hm.items() if val is not None}
print(cleaned_hm) # {'a': 1, 'b': 1}
# In-Place Removal (Memory Efficient)
try:
    for key, val in hm.items():
        if val is None:
            print(f"deleting: {val}")
            del hm[key]
except RuntimeError as error:
    print(error) # RuntimeError: dictionary changed size during iteration
# You cannot modify a dict while iterating over it.

# Correct way
for key in list(hm.keys()):
    if hm[key] is None:
        del hm[key]
print(hm) # {'a': 1, 'b': 1}