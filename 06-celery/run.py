from basics import remove_duplicates, fetch_data, fetch_data_slow

# Run the task using delay()
# remove_duplicates.delay()

# Running Tasks with custom queue

for _ in range(20):

    fetch_data.apply_async(args=('Netflix', 5), queue='high_priority')

for _ in range(20):
    fetch_data_slow.apply_async(args=('Amazon Prime', 10), queue='low_priority')