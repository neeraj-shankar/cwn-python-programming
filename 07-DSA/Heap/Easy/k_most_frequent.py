"""
Given an integer array nums and an integer k, return the k most frequent elements.
"""

from collections import Counter
class FrequentElements:

    def solution_hm_sorting(self, nums: list[int], k: int):

        hm = Counter(nums)

        sorted_list = sorted(hm.items(), key=lambda x: x[1], reverse=True)
        print(hm)
        print(sorted_list)

        return  [x[0] for x in sorted_list[0:k]]

if __name__ == "__main__":

    fe = FrequentElements()

    nums = [1,1,2,2,2,3]
    k = 2

    print(f"Top Frequent Elements: {fe.solution_hm_sorting(nums, k)}")


