"""
Python programing to demonstrate all the operation that can be performed using queue data structures
"""


# import format_output
class QueueImplementation:
    # Initialize the empty list
    def __init__(self):
        self.items = []

    def __str__(self):
        """
        Takes no argument. Convert Python list into queue readable format

        : params : No parameter required.
        : time complexity : O(n)
        : space complexity : o(n)
        : returns: list items as queue formatted items
        """
        values = [str(value) for value in self.items]
        return " ".join(values)

    def is_empty(self):
        """
        Takes no argument. Check the items list and evaluates whether the queue is empty or not.

        : params : Takes no aruguement.
        : time complexity : O(1)
        : space complexity : O(1)
        : return : True if Queue is empty and False if Queue has one or more elements
        """
        if not self.items:
            return True
        else:
            return False

    def push(self, element):
        """
        Takes the element as input and add it to the end of the queue.

        : param element : The element to be pushed to the queue.
        : time complexity : O(1)
        : space complexity : O(1)
        : return : The updated queue data

        """
        self.items.append(element)
        return self.items


"""
Class Object
"""

queue_implement = QueueImplementation()

# format_output.use_case_separator(f"Validating Is_empty() method...")
is_empty = queue_implement.is_empty()
print(f"Whether the queue is empty --> {is_empty}")

queue_implement.push(1)
queue_implement.push(2)
print(f"The updated queue --> {queue_implement.__str__()}")
is_empty = queue_implement.is_empty()
print(f"Whether the queue is empty --> {is_empty}")
