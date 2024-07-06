"""
There are two sorted arrays num1 and nums2 of size m and n repectively. 

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n))

You may assume nums1 and nums2 cannot be empty

eg -->  nums1 = [1, 3] and nums2 = [2]. The median is 2.0 

eg2 --> nums1 = [1, 2] and nums2 = [3, 4]. The median is (2 +3)/2 = 2.5
"""


class TwoArraysMedian:

    def find_by_sorted_method_technique(self, nums1, nums2): # Time Comlexity --> 

        merged_nums = sorted(nums1 + nums2) # -----------------------------> O((n+m)log(n+m))
        n = len(merged_nums) # --------------------------------------------> O(1)
        mid = n // 2 # --------------------------------------------> O(1)

        if n % 2 == 0: # --------------------------------------------> O(1)
            return (merged_nums[mid-1] + merged_nums[mid])/2 # --------------------------------------------> O(1)
        else:
            return merged_nums[mid] # --------------------------------------------> O(1)



    def find_by_two_pointer_approach(self, nums1, nums2):
        n = len(nums1) + len(nums2) # --------------------------------------------> O(1)
        mid = n // 2 # --------------------------------------------> O(1)
        print(f"I am middle --> {mid}")

        i = 0 # Pointer for nums1 # --------------------------------------------> O(1)
        j = 0 # Pointer for nums2 # --------------------------------------------> O(1)
        merged_nums = [] # --------------------------------------------> O(1)
        while i < len(nums1) and j < len(nums2): # --------------------------------------------> O(n + m)
            if nums1[i] <= nums2[j]: # --------------------------------------------> O(1)
                merged_nums.append(nums1[i]) # --------------------------------------------> O(1)
                print(f"Merged Array --> {merged_nums}") # --------------------------------------------> O(1)
                i += 1 # --------------------------------------------> O(1)
            else:
                merged_nums.append(nums2[j]) # --------------------------------------------> O(1)
                print(f"Merged Array --> {merged_nums}") # --------------------------------------------> O(1)
                j += 1 # --------------------------------------------> O(1)
            
            if len(merged_nums) > mid + 1: # --------------------------------------------> O(1)
                print(f"onto break") # --------------------------------------------> O(1)
                break


        # Handling remaining elements in num1
        while i < len(nums2): 
            merged_nums.append(nums2[i])
            if len(merged_nums) > mid + 1:
                print(f"onto break")
                break        

        # Handling remaining elements in nums2        
        while j < len(nums2):
            merged_nums.append(nums2[j])
            if len(merged_nums) > mid + 1:
                print(f"onto break")
                break

        if n % 2 == 0:
            return (merged_nums[mid-1] + merged_nums[mid]) / 2
        else:
            return (merged_nums[mid])


"""
object creation and function calls
"""
obj = TwoArraysMedian()

# nums1 = [1, 3, 5, 7, 9, 10, 12, 14, 67, 98]
# nums2 = [2, 4, 6, 8]


nums1= [1, 2]
nums2 = [3, 4]

first_method = obj.find_by_sorted_method_technique(nums1, nums2)
print(first_method)
second_method = obj.find_by_two_pointer_approach(nums1, nums2)
print(second_method)
