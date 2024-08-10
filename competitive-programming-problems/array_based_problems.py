"""
1. Calculate the number of times the highest and lowest records are broken.
"""

class ArrayBasedProblemSet:

    def __init__(self) -> None:
        pass

    @staticmethod
    def break_the_records(scores):
        """
        Calculate the number of times the highest and lowest records are broken.

        Given a list of scores, the function returns a list containing two integers:
        - The first integer is the count of how many times the highest score record was broken.
        - The second integer is the count of how many times the lowest score record was broken.

        Parameters:
        scores (list): A list of integers representing the scores.

        Returns:
        list: A list with two integers, [max_count, min_count], where max_count is the number of times
            the highest score increased, and min_count is the number of times the lowest score decreased.

            Explanation:
        -----------------------------------------------------------
        Game  Score  Minimum  Maximum   Min Max
            0      12     12       12       0   0
            1      24     12       24       0   1
            2      10     10       24       1   1
            3      24     10       24       1   1

        -----------------------------------------------------------
        """
        
        # Initialize the minimum and maximum with the first score in the list
        minimum = maximum = scores[0]
        
        # Initialize counters for the number of times minimum and maximum records are broken
        max_count = min_count = 0
        
        # Iterate over the scores, starting from the second score
        for score in scores[1:]:
            # If the current score is less than the current minimum, update minimum and increment min_count
            if score < minimum:
                minimum = score
                min_count += 1
            
            # If the current score is greater than the current maximum, update maximum and increment max_count
            elif score > maximum:
                maximum = score
                max_count += 1
        
        # Prepare the record list with the counts of breaking the maximum and minimum records
        record = [max_count, min_count]
        
        # Return the record list
        return record


    def break_the_records_list_comprehension(scores:list):

        highest_score, lowest_score = scores[0], scores[0]

        # Calculate the counts using list comprehension
        highest_count = sum(score > (highest_score := max(highest_score, score)) for score in scores[1:])
        lowest_count = sum(score < (lowest_score := min(lowest_score, score)) for score in scores[1:])

        return highest_count, lowest_count


    def count_divisible_pairs(arr, k):
        """
        Calculate the number of pairs in the array whose sum is divisible by a given integer.

        This function iterates through each unique pair of elements in the input array `arr`
        and counts the number of pairs whose sum is divisible by the integer `k`.

        Parameters:
        arr (list): A list of integers representing the input array.
        k (int): A positive integer against which the divisibility of the sum of pairs is checked.

        Returns:
        int: The count of pairs whose sum is divisible by `k`.

        Time Complexity: O(n^2), where n is the length of the input array `arr`.
                        This is due to the nested loop iterating over all possible pairs.
        Space Complexity: O(1), as no additional space is used that grows with the input size.

        Note:
        The function assumes that `arr` is a list of integers and `k` is a positive integer.
        """

        # Initialize the counter for the number of divisible pairs
        count = 0

        # Iterate over the array with two pointers to consider each unique pair
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                # Check if the sum of the current pair is divisible by k
                if (arr[i] + arr[j]) % k == 0:
                    # If divisible, increment the count
                    count += 1

        # Return the total count of divisible pairs
        return count


    def count_divisible_pairs_map(arr, k):
        """
        Calculate the number of pairs in the array whose sum is divisible by a given integer.

        This function uses a frequency map to count the occurrences of each remainder when
        the array elements are divided by `k`. It then calculates the number of pairs that
        can be formed with these remainders such that their sum is divisible by `k`.

        Parameters:
        arr (list): A list of integers representing the input array.
        k (int): A positive integer against which the divisibility of the sum of pairs is checked.

        Returns:
        int: The count of pairs whose sum is divisible by `k`.

        Time Complexity: O(n), where n is the length of the input array `arr`.
        Space Complexity: O(k), as additional space is used for the frequency map with at most k keys.
        """

        # Initialize the frequency map for remainders
        remainder_freq = [0] * k

        # Populate the frequency map with the remainders of the array elements when divided by k
        for num in arr:
            remainder_freq[num % k] += 1

        # Initialize the counter for the number of divisible pairs
        count = 0

        # Count pairs for the remainder 0 (they must be paired with themselves)
        count += (remainder_freq[0] * (remainder_freq[0] - 1)) // 2

        # Count pairs between remainders i and k-i
        for i in range(1, (k // 2) + 1):
            if i != k - i:  # Remainders are different
                count += remainder_freq[i] * remainder_freq[k - i]
            else:  # Remainders are the same, so pair them with themselves
                count += (remainder_freq[i] * (remainder_freq[i] - 1)) // 2

        return count


    def find_container_with_most_water_pointer(self, height):
        """
        Calculate the maximum area of water that can be contained between two lines.

        This method uses a two-pointer approach to find the maximum area of water that can be
        contained between two lines in a list of heights. The area is calculated by taking the
        minimum of the two heights and multiplying it by the distance between the two lines.

        Parameters:
        height (list): A list of integers representing the heights of the lines.

        Returns:
        int: The maximum area of water that can be contained.

        Time Complexity: O(n), where n is the length of the input list `height`.
        Space Complexity: O(1), as the space used does not depend on the input size.

        Example Usage:
        >>> container = ContainerWithMostWater()
        >>> container.naive_approach([1, 8, 6, 2, 5, 4, 8, 3, 7])
        49
        """

        # Initialize the maximum area to 0
        max_area = 0

        # Initialize two pointers, left at the beginning and right at the end of the list
        left = 0
        right = len(height) - 1

        # Loop through the heights and calculate the area between two lines
        while left < right:
            # Calculate the area between the lines at the left and right pointers
            area = min(height[left], height[right]) * (right - left)

            # Update the maximum area if the current area is larger
            max_area = max(max_area, area)

            # Move the left and right pointers closer to each other
            # Move the pointer pointing to the shorter line to try and find a taller line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        # Return the maximum area found
        return max_area

