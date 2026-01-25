import time
import requests

def fetch_price_sync(store_name, product_id):
    """Simulate fetching price from a store's API"""
    print(f"🔍 Starting request to {store_name}...")
    time.sleep(2)  # Simulating network delay
    price = hash(store_name + product_id) % 100 + 50  # Fake price
    print(f"✅ {store_name} responded: ${price}")
    return {store_name: price}

def compare_prices_sync(product_id):
    stores = ["Amazon", "Walmart", "Target", "BestBuy"]
    prices = {}
    
    start = time.time()
    for store in stores:
        result = fetch_price_sync(store, product_id)
        prices.update(result)
    
    elapsed = time.time() - start
    print(f"\n⏱️  Total time: {elapsed:.2f} seconds")
    return prices

# Run it
compare_prices_sync("laptop-123")

"""
# **Output:**
-----------------------------------------------------------
# 🔍 Starting request to Amazon...
# ✅ Amazon responded: $89
# 🔍 Starting request to Walmart...
# ✅ Walmart responded: $72
# 🔍 Starting request to Target...
# ✅ Target responded: $95
# 🔍 Starting request to BestBuy...
# ✅ BestBuy responded: $81
# ⏱️  Total time: 8.00 seconds
-----------------------------------------------------------
The Problem: Each request waits for the previous one to complete. 
Total time = 4 stores × 2 seconds = 8 seconds. 
The CPU is idle 99% of the time, just waiting for network responses!
"""

# Approach 2: Async/Await - The Efficient Way
import asyncio
import time

async def fetch_price_async(store_name, product_id):
    """Async version - can pause and resume"""
    print(f"🔍 Starting request to {store_name}...")
    
    # await tells Python: "I'm waiting for network I/O, go do other work!"
    await asyncio.sleep(2)  # Simulating network delay
    
    price = hash(store_name + product_id) % 100 + 50
    print(f"✅ {store_name} responded: ${price}")
    return {store_name: price}

async def compare_prices_async(product_id):
    stores = ["Amazon", "Walmart", "Target", "BestBuy"]
    
    start = time.time()
    
    # Create all tasks at once
    tasks = [fetch_price_async(store, product_id) for store in stores]
    
    # Run them concurrently!
    results = await asyncio.gather(*tasks)
    
    # Merge results
    prices = {}
    for result in results:
        prices.update(result)
    
    elapsed = time.time() - start
    print(f"\n⏱️  Total time: {elapsed:.2f} seconds")
    return prices

# Run the async function
asyncio.run(compare_prices_async("laptop-123"))

"""

**Output:**
```
🔍 Starting request to Amazon...
🔍 Starting request to Walmart...
🔍 Starting request to Target...
🔍 Starting request to BestBuy...
✅ Amazon responded: $89
✅ Walmart responded: $72
✅ Target responded: $95
✅ BestBuy responded: $81

⏱️  Total time: 2.00 seconds
```

**The Breakthrough:** All requests run concurrently! Total time ≈ **2 seconds** (the time of the slowest request), not 8 seconds!

---

## 🧠 How It Actually Works: The Mental Model

Think of async/await like a **restaurant kitchen** with one chef (single thread):

### Sequential Cooking (Blocking):
```
1. Start boiling pasta → Stand and watch it for 10 minutes → Serve
2. Start grilling steak → Stand and watch it for 8 minutes → Serve
3. Start baking cake → Stand and watch it for 15 minutes → Serve

Total: 33 minutes of standing around!
```

### Async Cooking (Non-blocking):
```
1. Start boiling pasta → Set timer → Go do other work
2. Start grilling steak → Set timer → Go do other work  
3. Start baking cake → Set timer → Go do other work
4. Wait for timers, serve as each completes

Total: ~15 minutes (longest task)

"""