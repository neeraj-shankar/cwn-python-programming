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

    # --- TODO 1: Schedule the API calls ---
    # Use asyncio.create_task() or asyncio.gather()
    # to start 3 API calls with different delays (e.g., 1s, 2s, 3s).
    results = await asyncio.gather(
        fetch_api_data("Netflix", 1),
        fetch_api_data("Amazon", 2),
        fetch_api_data("Flipkart", 3)
    )
    
    
    # --- TODO 2: Schedule the Heavy CSV processing ---
    # Since this is a BLOCKING function, you cannot 'await' it directly.
    # Use loop.run_in_executor(None, ...) to run it in a background thread.
    res = loop.run_in_executor(None, heavy_csv_processing)
    
    # --- TODO 3: Wait for everything to finish ---
    # Capture the results from all tasks.
    logging.info(f"Results: {results}")
    logging.info(f"Result from Blocking Task: {res}")
    end_time = time.perf_counter()
    logging.info(f"Total time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())