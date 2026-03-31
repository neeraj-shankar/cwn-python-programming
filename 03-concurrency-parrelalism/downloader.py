import asyncio
import random

async def download_file(file_id, size_mb):
    """Simulate downloading a file"""
    print(f"📥 Starting download: file_{file_id} ({size_mb}MB)")
    
    # Simulate download time based on file size
    download_time = size_mb * 0.5
    await asyncio.sleep(download_time)
    
    print(f"✅ Completed: file_{file_id}")
    return f"file_{file_id}.data"

async def process_file(filename):
    """Simulate processing a downloaded file"""
    print(f"⚙️  Processing {filename}...")
    await asyncio.sleep(1)  # Processing takes 1 second
    print(f"✨ Processed {filename}")
    return f"processed_{filename}"

async def download_and_process(file_id):
    """Download then process a single file"""
    size = random.randint(1, 4)
    filename = await download_file(file_id, size)
    result = await process_file(filename)
    return result

async def main():
    """Download and process multiple files concurrently"""
    print("🚀 Starting batch download and processing...\n")
    
    start = asyncio.get_event_loop().time()
    
    # Process 5 files concurrently
    tasks = [download_and_process(i) for i in range(1, 6)]
    results = await asyncio.gather(*tasks)
    
    elapsed = asyncio.get_event_loop().time() - start
    
    print(f"\n🎉 All done! Processed {len(results)} files")
    print(f"⏱️  Total time: {elapsed:.2f} seconds")
    print(f"📊 Results: {results}")

# Run it!
asyncio.run(main())