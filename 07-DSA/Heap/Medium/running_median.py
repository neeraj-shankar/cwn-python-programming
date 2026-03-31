"""
Given an array of integers, A denoting the delivery times for each order. 
New arrays of integer B and C are formed, each time a new delivery data is encountered, 
append it at the end of B and append the median of array B at the end of C. 
Your task is to find and return the array C.

NOTE:

1. If the number of elements is N in B and N is odd, then consider the median 
as B[N/2] ( B must be in sorted order).

2. If the number of elements is N in B and N is even, then consider the median 
as B[N/2-1]. ( B must be in sorted order).

"""
import heapq

class RunningMedian:

    def solution_heap(self, A: list[int])-> list[int]:
        pass

if __name__ == "__main__":

    rm = RunningMedian()

    # Test Case 1: 
    A = [1, 2, 5, 4, 3]
    print(f"Median:\n{rm.solution_heap(A)}")
