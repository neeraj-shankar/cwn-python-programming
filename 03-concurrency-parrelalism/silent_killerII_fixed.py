import asyncio
import time
import logging

# Setup logging to see the Thread IDs and timestamps
logging.basicConfig(
    format="%(asctime)s | TID:%(thread)d | %(message)s", 
    level=logging.INFO
)

async def fetch_api_data(name, delay):
    logging.info(f"API {name}: Starting request...")
    await asyncio.sleep(delay)
    logging.info(f"API {name}: Data received after {delay}s")
    return f"{name} data"

def heavy_csv_processing():
    """This is a synchronous, blocking function."""
    logging.info("CSV: Starting heavy processing (Blocking)...")
    time.sleep(4)  # Simulating heavy CPU/IO work
    logging.info("CSV: Processing finished.")
    return "Processed CSV"

async def main():
    start_time = time.perf_counter()
    loop = asyncio.get_running_loop()
    # 1. Start the blocking task in the background (Returns a Future)
    # We don't await it yet!
    csv_future = loop.run_in_executor(None, heavy_csv_processing)

    # 2. Start the API calls (Returns a Coroutine/Future)
    # We use gather to group them   
    api_group = asyncio.gather(
        fetch_api_data("Netflix", 1),
        fetch_api_data("Amazon", 2),
        fetch_api_data("Flipkart", 3)
    )

    # 3. NOW we await everything together
    # This ensures the 4s CSV and 3s APIs run at the same time
    api_results, csv_result = await asyncio.gather(api_group, csv_future)
    logging.info(f"Results: {api_results}")
    logging.info(f"Result from Blocking Task: {csv_result}")
    
    end_time = time.perf_counter()
    logging.info(f"Total time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())