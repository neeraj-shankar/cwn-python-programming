from collections import deque

## Using deque as Queue
## Insert from right and remove from left.
my_queue = deque();
print(f"Current Status of Deque: ",my_queue)
my_queue.append(2);
my_queue.append(3);
print(f"Current Status of Deque: ",my_queue)
print(my_queue.popleft())
