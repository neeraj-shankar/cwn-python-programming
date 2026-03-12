"""
Let's say we want to resize the (eg, square the size) for 1000 images (images size) passed as a list.

Instead of doing them one by one, we'll throw them into a pool.
"""

import multiprocessing 
import time

def resize_images(size: int):

    # Square the size of the image and return it
    return size * size

if __name__ == "__main__":

    sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Create a Pool of workers. 
    # Usually, we set this to the number of CPU cores we have.
    # If you don't specify, it defaults to your total CPU count.
    with multiprocessing.Pool(processes=4) as pool:

        # 'map' is the magic word. 
        # It sends the 'sizes' list to the 'resize_images' function 
        # using the 4 workers in the pool.
        results = pool.map(resize_images, sizes)

    print(f"All task completed..")
    print(results)

