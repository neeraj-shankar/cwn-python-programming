"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such 
that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that 
the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) 
the container can contain is 49.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49

"""

class MaxAreaCalculation:

    def naive_approach(self, height):

        max_area = 0
        left = 0
        right = len(height)-1

        # Loop through the heights and calculate area between two lines
        while left < right:
            area = min(height[left], height[right]) * (right - left)

            # update the max area
            max_area = max(max_area, area)

            # move left and right pointer closer to each other
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


"""
In this code, the function max_area takes a list of integers height as input and returns the maximum area of water that can be contained between two lines.

The two-pointer approach is used to find the maximum area. The left pointer starts from the leftmost line, and the right pointer starts from the 
rightmost line. The area between the two lines is calculated as the minimum height of the two lines multiplied by the distance between them.

The algorithm starts with the widest container (the maximum distance between the lines) and then moves the pointers towards each other 
while keeping track of the maximum area found so far. The pointers are moved based on the height of the lines to explore potentially greater areas.

Finally, the function returns the maximum area found.
"""
obj = MaxAreaCalculation()

heights = [1,8,6,2,5,4,8,3,7]
result = obj.naive_approach(heights)
print(result)