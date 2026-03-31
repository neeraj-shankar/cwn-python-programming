import asyncio

async def fetch_data():
    print("Start fetching data...")
    await asyncio.sleep(2)  # Simulate a network request with a delay of 2 seconds
    print("Done fetching data")
    return {"data": "Sample Data"}

async def process_data():
    print("Start processing data...")
    await asyncio.sleep(1)  # Simulate some data processing with a delay of 1 second
    print("Done processing data")
    return "Processed Data"

async def main():
    # Run both tasks concurrently
    fetch_task = asyncio.create_task(fetch_data())
    process_task = asyncio.create_task(process_data())
    
    # Wait for both tasks to complete
    fetched_data = await fetch_task
    processed_data = await process_task
    
    print(f"Fetched Data: {fetched_data}")
    print(f"Processed Data: {processed_data}")

# Run the event loop
asyncio.run(main())
