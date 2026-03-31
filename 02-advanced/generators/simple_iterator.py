class SimpleIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
        print(f"Created iterator with data: {data}, index: {self.index}")
    
    def __iter__(self):
        print(f"__iter__ called, returning self")
        return self
    
    def __next__(self):
        print(f"__next__ called, current index: {self.index}")
        
        if self.index >= len(self.data):
            print("No more items, raising StopIteration")
            raise StopIteration
        
        value = self.data[self.index]
        self.index += 1
        print(f"Returning: {value}, next index will be: {self.index}")
        return value

# Watch the execution
print("=== Creating iterator ===")
my_iter = SimpleIterator(['A', 'B', 'C'])

print("\n=== Starting for loop ===")
for item in my_iter:
    print(f"Got item in loop: {item}\n")

# **Output:**
# ```
# === Creating iterator ===
# Created iterator with data: ['A', 'B', 'C'], index: 0

# === Starting for loop ===
# __iter__ called, returning self
# __next__ called, current index: 0
# Returning: A, next index will be: 1
# Got item in loop: A

# __next__ called, current index: 1
# Returning: B, next index will be: 2
# Got item in loop: B

# __next__ called, current index: 2
# Returning: C, next index will be: 3
# Got item in loop: C

# __next__ called, current index: 3
# No more items, raising StopIteration
