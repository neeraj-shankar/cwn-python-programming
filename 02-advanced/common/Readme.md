# Comonly Used Advanced Concepts

## Packing and Upacking
- Packing happens when you take multiple values and assign them to a single variable. Python automatically "packs" them into a tuple.

```python
my_stuff = "Laptop", "Coffee", 42 

print(my_stuff) # Output: ('Laptop', 'Coffee', 42)
```

- Unpacking is the reverse. You take an iterable (like a list or tuple) and split its contents into separate variables.

```python
# The "package"
coordinates = (10, 20)

# Unpacking it
x, y = coordinates

print(x) # 10
print(y) # 20
```

- **Advanced Unpacking (Extended Iterable Unpacking):** Sometimes you don't want every single item, or you don't know how many items there are. This is where the star operator **(*)** comes in.
```python
scores = [98, 85, 70, 60, 42]

highest, *middle, lowest = scores

print(highest) # 98
print(middle)  # [85, 70, 60]
print(lowest)  # 42
```
