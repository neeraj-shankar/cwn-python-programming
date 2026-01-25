import asyncio
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | PID:%(process)d | TID:%(thread)d | %(funcName)s | %(levelname)s | %(message)s"
)

async def hello_async_world():
    logging.info(f"Fetching data.....")
    await asyncio.sleep(2)
    logging.info(f"Data is received.....")


asyncio.run(hello_async_world())

# run multiple tasks at once using asyncio.gather()

async def fetch_service(service, delay):
    logging.info(f"Fetching data from service: {service}")
    await asyncio.sleep(delay)
    return f"Data from {service}"


async def main():

    start = time.perf_counter()

    # Scheduling five tasks to run concurrently
    results = await asyncio.gather(
        fetch_service("Netflix", 5),
        fetch_service("Amazon Prime", 10),
        fetch_service("Hotstar", 5),
        fetch_service("Sony Liv", 15),
        fetch_service("other", 12)
    )

    end = time.perf_counter()

    logging.info(f"Results: {results}")
    logging.info(f"All data fetched within {end - start:.2f} seconds")

asyncio.run(main())