import asyncio
import time

# Scenario: User closes browser while data is being fetched
async def fetch_user_data(user_id, duration=10):
    """Simulates a 10-second API call"""
    print(f"[{time.time():.2f}] Fetching user {user_id}...")
    try:
        await asyncio.sleep(duration)
        print(f"[{time.time():.2f}] ✅ User {user_id} fetched")
        return {"id": user_id, "name": "John"}
    except asyncio.CancelledError:
        print(f"[{time.time():.2f}] ⚠️  User {user_id} fetch cancelled - cleaning up")
        # Clean up resources (close connections, release locks, etc.)
        raise  # Important: re-raise to propagate cancellation

async def web_request_handler(user_id):
    """Simulates a web request that might be cancelled"""
    task = asyncio.create_task(fetch_user_data(user_id, duration=10))
    
    # Simulate user closing browser after 2 seconds
    await asyncio.sleep(2)
    print(f"\n>>> User closed browser! Cancelling request...\n")
    task.cancel()
    
    try:
        result = await task
    except asyncio.CancelledError:
        print("Request handling complete (task was cancelled)")
    
    # Important: Check if we should return error response
    # Don't leave resources hanging!

asyncio.run(web_request_handler("user_123"))