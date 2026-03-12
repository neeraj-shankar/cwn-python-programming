import requests
from concurrent.futures import ThreadPoolExecutor
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | PID:%(process)d | TID:%(thread)d | %(funcName)s | %(levelname)s | %(message)s"
)

# A list of URLs to scrape (you can add as many as you want)
urls = [
    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.python.org",
    "https://www.github.com",
    "https://www.reddit.com"
]

def fetch_urls(url):
    """Function to download a single page"""
    logging.info(f"Starting Download from {url}")

    try:
        response = requests.get(url=url, timeout=5)
        # We just return the length of the text as a 'result'
        return f"{url} is {len(response.text)} characters long."
    
    except Exception as e:
        logging.info(f"Error scrapping {url}: {e}")


def run_multithreaded():

    start = time.time()

    # Create of pool threads
    # 'max_workers' is how many 'chefs' are in our kitchen
    with ThreadPoolExecutor(max_workers=5) as executor:
        # .map() sends the list of URLs to the fetch_url function
        results = executor.map(fetch_urls, urls)

    # Display the results
    for result in results:
        print(result)

    end = time.time()
    print(f"\n Total time taken with Threads: {end-start:.2f} seconds.")

if __name__ == "__main__":

    run_multithreaded()