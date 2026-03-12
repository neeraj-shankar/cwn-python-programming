"""
You are given a Max-Heap represented as a Python list.

In a Max-Heap, the value at each parent node is greater than or equal to the values of its children.

The heap follows 0-based indexing, where:

For a node at index i:
Parent is at index (i - 1) // 2
Left child is at index 2*i + 1
Right child is at index 2*i + 2
"""

class InsertElement:

    def solution(self, heap: list[int], element: int):

        heap.append(element)

        return self.up_heapify(heap)

    def up_heapify(self, heap: list[int]):

        n = len(heap)
        pos = n-1
        while(pos > 0):
            parentpos = (pos-1)//2

            if heap[pos] <= heap[parentpos]:
                break
            else:
                # print(f"swapping {heap[pos]} and {heap[parentpos]}")
                self.swap(heap, pos, parentpos)
                pos = parentpos
            print(heap)
        return heap

    def swap(self, nums: list[int], left: int, right: int)-> None:

        nums[left], nums[right] = nums[right], nums[left]


if __name__ == "__main__":

    ie = InsertElement()

    # Test Case 1: 
    heap = [9, 7, 8, 3, 2, 5] 
    x = 10
    print(f"Heap After Insertion:\n{ie.solution(heap, x)} ") # [10, 7, 9, 3, 2, 5, 8]

    # Test Case 2: Inserting a Value Smaller Than All Existing Elements
    heap = [9, 7, 8, 3, 2] # [9, 7, 8, 3, 2, 1]
    x = 1
    print(f"Heap After Insertion:\n{ie.solution(heap, x)} ")

    # Test Case 3: Inserting a Value Larger Than All Existing Elements
    heap = [9, 7, 8, 3, 2, 5] # [10, 7, 9, 3, 2, 5, 8]
    x = 10
    print(f"Heap After Insertion:\n{ie.solution(heap, x)} ") 

    # Test Case 4A: Duplicate Equal to Root
    heap = [10, 8, 9, 3, 2] # [10, 8, 10, 3, 2, 9]
    x = 10
    print(f"Heap After Insertion:\n{ie.solution(heap, x)} ")

    # Test Case 4B: Multiple Duplicates in Heap
    heap = [7, 7, 6, 5, 7] # [7, 7, 7, 5, 7, 6]
    x = 7
    print(f"Heap After Insertion:\n{ie.solution(heap, x)} ")

    # Test Case 6: Empty or single valued
    heap = [11]
    x = 10
    print(f"Heap After Insertion:\n{ie.solution(heap, x)} ")










        
