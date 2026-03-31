from collections import defaultdict

"""
Merge Dictionary:
1. Given two dictionary merge them. if values are overlapping sum them up.

"""
a = {'a': 1, 'b': 1, 'c': 1}
b = {'a': 1, 'c':1, 'd':1, 'e':1}

# 1. Naive approach --> create a result dictionary and one by one.
# Add first dictionary to res.
result = {}
for key, val in a.items():
    result[key] = val

# Update the result dictionary with second input dictionary
for key, val in b.items():
    result[key] = result.get(key, 0) + val

print(result)

#2. Using Default dict.
result = defaultdict(int)
for key, val in a.items():
    result[key] = val
for key,val in b.items():
    result[key] += val
print(result)
