class Queue:
    def __init__(self, max_size) -> None:
        self.items = max_size * [None]
        self.max_size = max_size
        self.start = -1
        self.end = -1

    def __str__(self) -> str:
        values = [str(x) for x in self.items]
        return "".join(values)

    def is_full(self):
        if self.end + 1 == self.start:
            print(f"First condition met")
            return True
        elif self.start == 0 and self.end + 1 == self.max_size:
            return True
        else:
            return False
    
    def is_empty(self):
        if self.end == -1:
            return True
        else:
            return False
    
    def enqueue(self, value):
        if self.is_full():
            return "The queue is full."
        else:
            if self.end + 1 == self.max_size:
                self.end = 0
                print(f"The end is reset --> {self.end}")
            else:
                self.end += 1
                print(f"The end point moved right --> {self.end}")
                if self.start == -1:
                    self.start = 0
            self.items[self.end] = value
            return f"The item {value} insterted at end of the queue"
        
    def dequeue(self):
        if self.is_empty():
            return f"The queue is empty."
        else:
            first_element = self.items[self.start]
            start = self.start
            if self.start == self.end:
                self.start = -1
                self.end = -1
            elif self.start + 1 == self.max_size:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return first_element 


"""
Create the object of the class Queue, Function call, input data 
"""
queue_size = 5
custom_queue = Queue(queue_size)

# print(custom_queue.is_empty())
# print(custom_queue.is_full())
# print(custom_queue.enqueue(1))
# print(custom_queue.enqueue(2))
# print(custom_queue.enqueue(3))
# print(custom_queue.enqueue(4))
# print(custom_queue.enqueue(5))
# print(custom_queue.enqueue(6))
print(custom_queue.dequeue)
print(custom_queue.dequeue)
print(custom_queue.items)