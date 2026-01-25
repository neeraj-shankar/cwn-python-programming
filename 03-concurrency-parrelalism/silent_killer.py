"""
show you how to "break" the event loop by accidentally putting a blocking task inside it? 
(This is the most common mistake senior devs make with async).
"""
import asyncio
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | PID:%(process)d | TID:%(thread)d | %(funcName)s | %(levelname)s | %(message)s"
)

async def asycn_task(name, duration):
    logging.info(f"Sending request to {name}" )
    await asyncio.sleep(duration)
    return f"Result Received from {name}"

async def blocking_task(name, duration):
    logging.info(f"BLOCKING TASK !!!! Sending request to {name}" )
    time.sleep(duration) # blocks other tasks. 
    return f" !! BLOCKING TASK FINISHED !!! Result Received from {name}" 

async def main():
    start = time.perf_counter()
    loop = asyncio.get_running_loop()
    results = await asyncio.gather(
        asycn_task("Netflix", 5),
        asycn_task("Amazon Prime", 10),
        # blocking_task("ZEE Prime", 15), # Blocks the other tasks after it
        # Fix run it on a seperate thread.
        loop.run_in_executor(None, blocking_task, "ZEE Prime", 10),
        asycn_task("Hotstar", 10)
    )

    end = time.perf_counter()
    logging.info(f"Entire request took {end-start:.2f}")

asyncio.run(main())


