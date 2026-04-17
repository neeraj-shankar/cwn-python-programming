class SortedArrayMerger:
    
    def solve(self, nums1, m, nums2, n):
        """
        1. Create three pointers:
            a. r1 --> tracks nums1
            b. r2 --> tracks nums2
            c. j --> trackers current fill valid place
            
        2. Compare elements from nums1 and nums2, move the largest element 
            at the end move j pointer backward
            
        3. Do this operation till r1 or r2 exchausts. 
        
        4. Check nums2 for any left numbers and add it to the array 
        """
        
        
        r1 = m-1
        r2 = m-1
        j = m + n -1 
        
        while r1 >= 0 and r2 >= 0:
            print(f" r1: {r1}, r2: {r2}, j: {j}")
            print(F"Array Status: {nums1}")
            if nums1[r1] <= nums2[r2]:
                nums1[j] = nums2[r2]
                r2 -= 1 
                
            else:
                nums1[j] = nums1[r1]
                r1 -= 1 
            
            j = j - 1 
        
        print(nums1)
        # Check and add leftover element from nums2
        while r2 >=0:
            
            nums1[j] = nums2[r2]
            r2 = r2 - 1 
            j = j -1 
            
        
        return nums1
    
if __name__ == "__main__":
    
    sam = SortedArrayMerger()
    
    nums1 = [1,2,3,0,0,0] 
    m = 3 
    nums2 = [2,5,6] 
    n = 3
    print("Merged Array: ", sam.solve(nums1, m, nums2, n))
        