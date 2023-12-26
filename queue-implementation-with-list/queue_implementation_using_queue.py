"""
In the program we will use deque module from collections to implement queue methods
"""
from collections import deque
class QueueImplementationWithCollection:

    def __init__(self):
        self.queue = deque()
    
    def __str__(self):
        values = self.queue
        return values

    def is_empty(self):
        """
        Takes no arguement. Check whether the queue is empty or has one more item
        
        : return : True if the Queue is empty and False if the Queue has one more item.
        """

        return True if len(self.queue) == 0 else False
    
    def enqueue(self, item):
        """
        Take the item as imput and add it the end of the queue

        : param item : The element to be inserted into the existing queue
        : return : None
        """
        self.queue.append(str(item))
    



"""
Class object and function call
"""

queue_obj = QueueImplementationWithCollection()


# checking status of queue before adding any element
queue_status = queue_obj.is_empty()
print(f"Is the current status of the queue empty --> {queue_status}")

# adding elements to the queue
for i in range(1, 5):
    queue_obj.enqueue(i)

print(f"The updated status of the Queue: ")
print(queue_obj.__str__())

# checking status of queue after adding any element
queue_status = queue_obj.is_empty()
print(f"Is the current status of the queue empty --> {queue_status}")