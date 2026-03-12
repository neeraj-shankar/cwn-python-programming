from utils import calculate_execution_time, async_timing
import asyncio
@async_timing
async def fetch_data(name, duration):
    print(f"Sending to request to fetch data from {name}")
    await asyncio.sleep(5)
    return f"Data fetched from {name} in duration {duration}"

asyncio.run(fetch_data("Netflix", 20))

fetch_data('Amazon', 5)