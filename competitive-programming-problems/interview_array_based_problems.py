class InterviewArrayQuestion:

    def __init__(self) -> None:
        pass

    def remove_duplicates_sorted_array(self, arr):
        """
        Remove some duplicates from a sorted array in-place such that each unique element appears at most twice.

        Args:
        nums (List[int]): The input list of integers sorted in non-decreasing order.

        Returns:
        int: The number of elements remaining in the list after removal.
        """
        
        if len(arr) <= 2:
            return len(nums)

        j = 2  # Initialize the pointer j to the third element

        for i in range(2, len(arr)):
            if arr[i] != arr[j - 2]:
                arr[j] = arr[i]
                j += 1
        
        return j  # j is the length of the modified array
        # Modified array: [1, 1, 2, 2, 3], Length of array after removal: 5

    def can_make_vertical_cut(toppings):
        """
        Determine if a vertical cut can be made through the cake such that:
        1. The cut does not intersect any toppings.
        2. Both resulting pieces of the cake contain at least one topping.

        Args:
        toppings (List[Tuple[int, int, int, int]]): List of toppings with their positions [start_x, end_x, start_y, end_y].

        Returns:
        bool: True if such a cut is possible, False otherwise.
        """
        
        # Extract the x-ranges of the toppings
        x_ranges = [(start_x, end_x) for (start_x, end_x, start_y, end_y) in toppings]
        
        # Sort the toppings based on their starting x positions
        x_ranges.sort()
        
        # Iterate through the sorted list and check for a valid cut
        for i in range(1, len(x_ranges)):
            if x_ranges[i-1][1] < x_ranges[i][0]:  # check for a gap between adjacent toppings
                return True  # Found a valid place to make the cut
        
        return False  # No valid cut found

    # Example usage:
    toppings = [(1, 3, 1, 2), (5, 7, 1, 2), (8, 10, 1, 2)]
    result = can_make_vertical_cut(toppings)
    print(f"Can make a vertical cut: {result}")

if __name__ == "__main__":

    nums = [1, 1, 1, 2, 2, 3]
    result = InterviewArrayQuestion().remove_duplicates_sorted_array(nums)
    print(f"Modified array: {nums[:result]}, Length of array after removal: {result}")
