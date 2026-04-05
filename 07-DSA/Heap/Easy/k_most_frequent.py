"""
Given an integer array nums and an integer k, return the k most frequent elements.
"""

from collections import Counter
import heapq
class FrequentElements:

    def solution_hm_sorting(self, nums: list[int], k: int):

        hm = Counter(nums)
        print(hm.get(2))

        sorted_list = sorted(hm.items(), key=lambda x: x[1], reverse=True)
        print(hm)
        print(sorted_list)

        return  [x[0] for x in sorted_list[0:k]]
    

    def solution_heap(self, nums: list[int], k: int):

        hm = Counter(nums)

        heap = []

        for num, count in hm.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)

        print(heap)
        return [num for count, num in heap]

if __name__ == "__main__":

    fe = FrequentElements()

    nums = [1,1,2,2,2,3]
    k = 2

    print(f"Top Frequent Elements: {fe.solution_hm_sorting(nums, k)}")
    print(f"Top Frequent Elements: {fe.solution_heap(nums, k)}")



