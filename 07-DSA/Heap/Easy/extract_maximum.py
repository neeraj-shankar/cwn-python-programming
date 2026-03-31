"""
You are given a Max-Heap represented as a Python list.

In a Max-Heap, the value at each parent node is greater than or equal to the values of its children.
The heap follows 0-based indexing, where:

For a node at index i:
Left child is at index 2*i + 1
Right child is at index 2*i + 2
Parent is at index (i - 1) // 2

"""
import heapq
class ExractMaximum:


    def down_heapify(self, heap: list[int])-> int:
        """
        Algorithm
        -----------------------------------------
        1. Swap the first element with last element of heap structure
        2. remove the last element now.
        3. balance the heap by making sure each parent is larger or equal than its children
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
            gei = i
            if lci < n and heap[gei] < heap[lci]:
                gei = lci
            
            if rci < n and heap[gei] < heap[rci]:
                gei = rci

            if gei == i:
                print(f"Heap Structure after removal:\n{heap}")
                break # No need to balance, parent already smaller than both children
            elif gei == lci:

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

    em = ExractMaximum()

    # Test case 1:
    heap = [9, 7, 8, 3, 2, 5]
    print(f"Largest Element: {em.down_heapify(heap)}") # [8, 7, 5, 3, 2]

    # Test Case 2: Heap with Duplicate Values
    heap = [6, 6, 5, 6, 4] 
    print(f"Largest Element: {em.down_heapify(heap)}") # [6, 6, 5, 4]

    # Test Case 3: Heap with Negative Numbers
    heap = [-1, -3, -2, -7, -6]
    print(f"Largest Element: {em.down_heapify(heap)}") # [-2, -3, -6, -7]


