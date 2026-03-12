"""
Design a function to extract and return the minimum element from the Min-Heap 
while preserving the heap property after removal.
"""

class SmallestElement:


    def down_heapify(self, heap: list[int])-> int:
        """
        Algorithm
        -----------------------------------------
        1. Swap the first element with last element of heap structure
        2. remove the last element now.
        3. balance the heap by making sure each parent is smaller than its children
        4. The children of any parent are given as:
            left child: 2*i + 1
            right child: 2*i + 2
        """

        n = len(heap)
        # Swap first and last
        heap[0], heap[n-1] = heap[n-1], heap[0]

        # Remove and return the last element
        ans = heap.pop()
        n = n-1

        # Balance the heap
        i=0
        while(2*i + 1 < n):
            lci = 2*i + 1
            rci = 2*i + 2
            # Get the minimum of three
            smallest = heap[i] 
            if lci < n-1 and heap[lci] < smallest:
                smallest = heap[lci] 
            
            if rci < n-1 and heap[rci] < smallest:
                smallest = heap[rci] 

            if smallest == heap[i]:
                print(f"Heap Structure after removal:\n{heap}")
                return ans # No need to balance, parent already smaller than both children
            elif smallest == heap[lci]:

                # Swap the parent with left child
                self.swap(heap, i, lci)
                i = lci
            else:
                # Swap the parent with right child
                self.swap(heap, i, rci)
                i = rci

        print(f"Heap Structure after removal:\n{heap}")

        return ans 
    
    def swap(self, nums: list[int], left: int, right: int)-> None:

        nums[left], nums[right] = nums[right], nums[left]
    
if __name__ == "__main__":

    se = SmallestElement()

    # Test case 1:
    heap = [1, 3, 5, 7, 9, 8]
    print(f"Smallest Element: {se.down_heapify(heap)}") # [3, 7, 5, 8, 9]

    # Test Case 2: Single Element Heap
    heap = [10]
    print(f"Smallest Element: {se.down_heapify(heap)}") # []

    # Test Case 3: Heap with Duplicate Values
    heap = [2, 2, 3, 5, 2]
    print(f"Smallest Element: {se.down_heapify(heap)}") # [2, 2, 3, 5]

    # Test Case 4: Heap with Negative Numbers
    heap = [-10, -3, 0, 5, 9, 2]
    print(f"Smallest Element: {se.down_heapify(heap)}") # [-3, 2, 0, 5, 9]

    # Test Case 5: Heap Already Almost Sorted
    heap = [0, 1, 2, 3, 4, 5]
    print(f"Smallest Element: {se.down_heapify(heap)}") # [1, 3, 2, 5, 4]







