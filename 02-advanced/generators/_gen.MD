# Generators and Iterators

## Generators

*The Real-Life Analogy: Netflix vs. Downloading Movies*

**Traditional Function (Downloading):**
- Imagine you want to watch a 10-season TV series. You download ALL 10 seasons (100+ GB) to your device before watching anything. You need massive storage space upfront, even though you're only watching one episode at a time.

**Generator (Streaming):**
- With Netflix, you stream one episode at a time. The next episode only loads when you're ready for it. You use minimal memory because you're only handling one episode at a time.

- That's exactly how generators work! They produce values one at a time, only when requested, instead of creating everything upfront.

- The key difference is yield instead of return. When you use yield, Python remembers where it left off and continues from there next time.

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

## The Two-Concept System - Iterables and Iterators
- Python has TWO related but different concepts:

### 1. Iterable (the container)
- An object that can be iterated over - it can give you an iterator.

```python
# These are all iterables
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_string = "abc"
my_dict = {'a': 1, 'b': 2}
my_set = {1, 2, 3}

# Generators are also iterables
my_generator = (x for x in range(3))
```
### 2. Iterator (the bookmark)
- An object that keeps track of position and can give you the next item.

```python
my_list = [1, 2, 3]
iterator = iter(my_list)  # Get the iterator from iterable

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
print(next(iterator))  # StopIteration exception - we've reached the end!
```
**Note** Generators are just convenient ways to create iterators! Python handles __iter__ and __next__ for you.