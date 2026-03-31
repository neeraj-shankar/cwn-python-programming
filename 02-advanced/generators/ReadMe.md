# Generators and Iterators

## Generators
In Python, generators are a special type of function that allow you to iterate over a sequence of values without creating the entire sequence in memory at once. They are "lazy," meaning they only produce the next item when specifically asked for it.

### Why Use Generators?
- Standard functions use return to send back a value and then terminate. 
- Generators use yield. When a generator yields a value, it pauses its execution state—including variable values and the instruction pointer—and resumes exactly where it left off the next time it's called.

1. **Memory Efficiency:** You can process a file with a billion lines without loading the whole file into RAM.

2. **Infinite Sequences:** You can represent a sequence that never ends (like a stream of sensor data).

### Understanding the Iterator Protocol
For a Python class to behave like a generator (becoming an "iterator"), it must implement two "dunder" (double underscore) methods:

1. `__iter__()`: Returns the iterator object itself. This allows the object to be used in for loops.

2. `__next__()`: Returns the next value in the sequence. If there are no more items, it must raise a StopIteration exception.

### Real Use Cases

- Reading a 10GB log file line by line:
```python
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Uses minimal memory, even for huge files
for line in read_large_file('huge_log.txt'):
    if 'ERROR' in line:
        print(line)
```

- **Processing data in stages without storing intermediate results:**
```python
def read_sensor_data():
    """Simulate reading from sensors"""
    for i in range(1000000):
        yield {'temp': 20 + i * 0.01, 'humidity': 50 + i * 0.005}

def filter_high_temp(data_stream):
    """Filter data on the fly"""
    for reading in data_stream:
        if reading['temp'] > 25:
            yield reading

def format_alert(filtered_stream):
    """Format filtered data"""
    for reading in filtered_stream:
        yield f"ALERT: Temp {reading['temp']}°C"

# Chain them together - no intermediate storage!
alerts = format_alert(filter_high_temp(read_sensor_data()))
for alert in alerts:
    print(alert)
```

- Batch Processing APIs: When fetching paginated data from APIs:
```python
def fetch_all_users(api_client):
    page = 1
    while True:
        users = api_client.get_users(page=page)
        if not users:
            break
        for user in users:
            yield user
        page += 1

# Process users one at a time as they're fetched
for user in fetch_all_users(api):
    process_user(user)
```

### When Generators Help vs. When They Don't

#### ✅ Generators ARE helpful when:
- Dataset is too large for memory (reading from file/database/stream)
- You only need the first solution (can stop early)
- You need all solutions but want to process them one at a time
- Data is continuously arriving (sensors, APIs, logs)

#### ❌ Generators DON'T help when:
- You need random access to data (generators are sequential only)
- Dataset already fits comfortably in memory

**Note** Generators are just convenient ways to create iterators! Python handles __iter__ and __next__ for you.

## FAQs

### 1. Which of the following methods must a class implement to be considered an 'iterator' in Python?
- `iter()` and `next()`: The iterator protocol requires iter() to return the iterator itself and next() to return the next value.

### 2. What happens when the __next__() method is called on an iterator that has no more items to return?
- Python uses the **StopIteration** exception to signal that there are no further items produced by the iterator.

### 3. What is the primary keyword used to turn a standard function into a generator function?
- The yield keyword pauses function execution and saves its state, returning a value to the caller and making the function a generator.

### 4. Which of the following is a key advantage of using a generator over a list for processing large datasets?
- Generators use 'lazy evaluation,' meaning they only compute and store the current item in memory rather than the entire collection.

### 5. In a generator function, what happens to the local variables after a yield statement is executed?
- They are suspended and preserved until the generator is resumed.
- Generators maintain the entire local state, including variable values and the instruction pointer, between yields.

### 6.Which built-in Python function is used to manually obtain an iterator from an iterable (like a list or string)?
- The `iter()` function calls the iter() method of an object to return an iterator.

### 7. Consider this code: gen = (x**2 for x in range(3)). What is the result of calling list(gen) twice?
- [0, 1, 4] and []: 
- Once the generator reaches the end of its iteration, it remains exhausted and returns an empty result for subsequent attempts.

### 8. What is the purpose of the yield from statement introduced in Python 3.3?
- To delegate part of its operations to another iterable or generator.
- Yield from allows a generator to yield all values from another sub-generator or iterable directly.